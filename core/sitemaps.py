from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return [
            "pages:homepage",
            "pages:showreel",
            "pages:credits",
            "media:photo_list",
            "contact:contact",
                ]

    def location(self, item):
        return reverse(item)
    
sitemaps = {
    "static": StaticViewSitemap,
}   