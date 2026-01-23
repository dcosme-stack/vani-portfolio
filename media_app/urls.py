from django.urls import path
from . import views

app_name = "media"

urlpatterns = [
    path("photos/", views.photo_list, name="photo_list"),
    path("photos/<slug:category_slug>/", views.photo_list, name="photo_list_by_category"),

    path("videos/", views.video_list, name="video_list"),
    path("videos/<slug:category_slug>/", views.video_list, name="video_list_by_category"),
]