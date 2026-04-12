from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return [
            "pages:homepage",
            "pages:about",
            "pages:resume",
            "media:photo_list",
            "media:video_list",
            "contact:contact",
                ]

    def location(self, item):
        return reverse(item)
    
sitemaps = {
    "static": StaticViewSitemap,
}   