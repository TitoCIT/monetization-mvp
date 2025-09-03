from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return [
            "public_home",
            "public_features",
            "public_pricing",
            "public_faq",
            "public_about",
            "public_contacts",
            "public_login",
            "public_register",
            "public_privacy",
            "public_terms",
        ]

    def location(self, item):
        return reverse(item)
