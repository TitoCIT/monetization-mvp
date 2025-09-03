from rest_framework import serializers
from .models import Category, TimeEntry, Customer, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("user", "id", "created_at")


class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEntry
        fields = "__all__"
        read_only_fields = ("user", "id", "created_at")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        # organization виставляється у ViewSet автоматично; з клієнта не потрібно передавати
        read_only_fields = ("organization", "id", "created_at")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # organization виставляється у ViewSet автоматично; з клієнта не потрібно передавати
        read_only_fields = ("organization", "id", "created_at")
