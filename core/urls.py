from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # API роутинг твого застосунку
    path("api/", include("tracker.urls")),

    # OpenAPI schema (JSON)
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # Redoc UI
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

from core.views import (
    PublicHomeView,
    PublicFeaturesView,
    PublicPricingView,
    PublicFAQView,
    PublicAboutView,
    PublicContactsView,
    PublicLoginView,
    PublicRegisterView,
    AppDashboardView,
    AppCustomersListView,
    AppProductsListView,
)
from core.sitemaps import StaticViewSitemap

sitemaps_dict = { "static": StaticViewSitemap }
INSTALLED_APPS = [
    # ...
    "drf_spectacular",
]
urlpatterns = [
    path("admin/", admin.site.urls),

    # Public pages
    path("", PublicHomeView.as_view(), name="public_home"),
    path("features/",  PublicFeaturesView.as_view(), name="public_features"),
    path("pricing/",   PublicPricingView.as_view(), name="public_pricing"),
    path("faq/",       PublicFAQView.as_view(), name="public_faq"),
    path("about/",     PublicAboutView.as_view(), name="public_about"),
    path("contacts/",  PublicContactsView.as_view(), name="public_contacts"),
    path("login/",     PublicLoginView.as_view(), name="public_login"),
    path("register/",  PublicRegisterView.as_view(), name="public_register"),

    # Footer pages
    path("privacy/", TemplateView.as_view(template_name="public/privacy.html"), name="public_privacy"),
    path("terms/",   TemplateView.as_view(template_name="public/terms.html"),   name="public_terms"),

    # Robots & Sitemap
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_txt"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps_dict}, name="django.contrib.sitemaps.views.sitemap"),

    # App (organization) pages
    path("app/<str:org>/dashboard/", AppDashboardView.as_view(), name="app_dashboard"),
    path("app/<str:org>/customers/", AppCustomersListView.as_view(), name="app_customers"),
    path("app/<str:org>/products/",  AppProductsListView.as_view(), name="app_products"),

    # API & Auth
    path("api/", include("tracker.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
