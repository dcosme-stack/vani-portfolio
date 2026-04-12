from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home_view, name="homepage"),
    path("showreel/", views.showreel_view, name="showreel"),
    path("credits/", views.credits_view, name="credits"),
    path("credits/<slug:category_slug>/", views.credits_view, name="credits_list_by_category"),

]