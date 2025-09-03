from django.contrib import admin
from .models import Category, TimeEntry
from .models import Organization, Membership, Customer, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "color", "created_at")
    search_fields = ("name",)

@admin.register(TimeEntry)
class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "started_at", "ended_at", "created_at")
    list_filter = ("category",)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "organization", "role")
    list_filter = ("role", "organization")
    search_fields = ("user__username", "organization__name")

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "organization", "email", "phone", "created_at")
    list_filter = ("organization",)
    search_fields = ("name", "email", "phone")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "sku", "name", "organization", "price", "category", "created_at")
    list_filter = ("organization", "category")
    search_fields = ("sku", "name")

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "organization", "customer", "date", "total_amount")
    list_filter = ("organization", "date")
    inlines = [OrderItemInline]
