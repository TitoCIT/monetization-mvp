from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TimeEntryViewSet, CustomerViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"entries", TimeEntryViewSet, basename="timeentry")
router.register(r"customers", CustomerViewSet, basename="customer")
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = router.urls
