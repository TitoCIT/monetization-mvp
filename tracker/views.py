from django.db import IntegrityError
from rest_framework import viewsets, permissions, serializers
from rest_framework.exceptions import PermissionDenied

from .models import Category, TimeEntry, Membership, Customer, Product
from .serializers import (
    CategorySerializer,
    TimeEntrySerializer,
    CustomerSerializer,
    ProductSerializer,
)


# ===========================
#        DRF VIEWSETS
# ===========================
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TimeEntryViewSet(viewsets.ModelViewSet):
    serializer_class = TimeEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TimeEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ===========================
#       MULTI-ORG CORE
# ===========================
def get_user_active_organization(user):
    membership = (
        Membership.objects
        .filter(user=user)
        .select_related("organization")
        .first()
    )
    return membership.organization if membership else None


class IsAuthenticatedInOrg(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and get_user_active_organization(request.user)
        )


class OrgScopedModelViewSet(viewsets.ModelViewSet):
    """
    Базовий в’юсет, який автоматично фільтрує/створює об’єкти в межах active org
    і конвертує IntegrityError у 400 ValidationError.
    """
    permission_classes = [IsAuthenticatedInOrg]
    org_field_name = "organization"

    def get_queryset(self):
        org = get_user_active_organization(self.request.user)
        if not org:
            return self.queryset.none()
        return self.queryset.filter(**{self.org_field_name: org})

    def perform_create(self, serializer):
        org = get_user_active_organization(self.request.user)
        if not org:
            raise PermissionDenied("No active organization")
        try:
            serializer.save(**{self.org_field_name: org})
        except IntegrityError as e:
            raise serializers.ValidationError({"detail": str(e)})


class CustomerViewSet(OrgScopedModelViewSet):
    queryset = Customer.objects.all().order_by("-id")
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        org = get_user_active_organization(self.request.user)
        if not org:
            raise PermissionDenied("No active organization")
        name = serializer.validated_data.get("name")
        if name and Customer.objects.filter(organization=org, name=name).exists():
            raise serializers.ValidationError(
                {"name": ["Клієнт з таким ім'ям уже існує в цій організації."]}
            )
        return super().perform_create(serializer)


class ProductViewSet(OrgScopedModelViewSet):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        org = get_user_active_organization(self.request.user)
        if not org:
            raise PermissionDenied("No active organization")
        sku = serializer.validated_data.get("sku")
        if sku and Product.objects.filter(organization=org, sku=sku).exists():
            raise serializers.ValidationError(
                {"sku": ["Товар із таким SKU уже існує в цій організації."]}
            )
        return super().perform_create(serializer)
