from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home_view, name="homepage"),
    path("about/", views.about_view, name="about"),
    path("resume/", views.resume_view, name="resume"),

]