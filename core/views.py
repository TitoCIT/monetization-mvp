from django.views.generic import TemplateView


# ===========================
#       PUBLIC PAGES
# ===========================
class PublicBaseView(TemplateView):
    """
    База для публічних сторінок: додає canonical_url та простий JSON-LD Organization.
    Шаблони можуть підміняти title/meta через {% block %} у base.html.
    """
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        req = self.request
        ctx["canonical_url"] = req.build_absolute_uri()
        ctx["schema_json"] = {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "Ozon Analytics",
            "url": req.build_absolute_uri("/"),
        }
        return ctx


class PublicHomeView(PublicBaseView):
    template_name = "public/home.html"


class PublicFeaturesView(PublicBaseView):
    template_name = "public/features.html"


class PublicPricingView(PublicBaseView):
    template_name = "public/pricing.html"


class PublicFAQView(PublicBaseView):
    template_name = "public/faq.html"


class PublicAboutView(PublicBaseView):
    template_name = "public/about.html"


class PublicContactsView(PublicBaseView):
    template_name = "public/contacts.html"


class PublicLoginView(PublicBaseView):
    template_name = "public/login.html"


class PublicRegisterView(PublicBaseView):
    template_name = "public/register.html"


# ===========================
#      APP (ORG) PAGES
# ===========================
class AppBaseView(TemplateView):
    """
    База для сторінок кабінету (noindex у шаблоні).
    Очікує параметр 'org' у URL.
    """
    template_name = "app/base_app.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["org"] = self.kwargs.get("org", "default")
        return ctx


class AppDashboardView(AppBaseView):
    template_name = "app/dashboard.html"


class AppCustomersListView(AppBaseView):
    template_name = "app/customers_list.html"


class AppProductsListView(AppBaseView):
    template_name = "app/products_list.html"


__all__ = [
    # Public
    "PublicHomeView",
    "PublicFeaturesView",
    "PublicPricingView",
    "PublicFAQView",
    "PublicAboutView",
    "PublicContactsView",
    "PublicLoginView",
    "PublicRegisterView",
    # App
    "AppDashboardView",
    "AppCustomersListView",
    "AppProductsListView",
]
