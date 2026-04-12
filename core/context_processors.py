from .models import SiteSettings
from django.urls import reverse
from .navigation import NAVIGATION

def site_settings(request):
    return {
        'site': SiteSettings.objects.first()
    }

def seo_metadata(request):
    """
    Provide default SEO metadata for all pages.
    Individual views can override by passing `seo` in context.
    """
    return {
        "seo": {
            "title": "Vanishree Kulkarni – Acting Portfolio",
            "description": "Official portfolio of Vanishree Kulkarni, featuring her acting roles, resume, photos, and videos.",
            "url": request.build_absolute_uri(),
            "image": request.build_absolute_uri("/static/images/og-default.jpg"),
            "twitter_card": "summary_large_image",
        }
    }

def navigation(request):

    desktop = []
    mobile = []
    footer = []

    for item in sorted(NAVIGATION, key=lambda x: x.get("order", 0)):

        nav_item = {
            "label": item["label"],
            "url": reverse(item["url_name"]),
            "active_prefix": item["active_prefix"],
        }

        if "desktop" in item["locations"]:
            desktop.append(nav_item)
        if "mobile" in item["locations"]:
            mobile.append(nav_item)
        if "footer" in item["locations"]:
            footer.append(nav_item)

    return {
        "desktop_nav": desktop,
        "mobile_nav": mobile,
        "footer_nav": footer,
    }