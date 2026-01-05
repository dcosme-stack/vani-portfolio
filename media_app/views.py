from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from .models import Photo, Video, Category

# Create your views here.
VALID_CATEGORIES = [choice[0] for choice in Category.choices]


def photo_list(request, category=None):
    photos = Photo.objects.all().order_by("-created_at")

    if category:
        if category not in VALID_CATEGORIES:
            raise Http404
        photos = photos.filter(category=category)

    return render(request, "media/photos.html", {
        "photos": photos,
        "categories": Category.choices,
        "current_category": category,
    })


def video_list(request, category=None):
    videos = Video.objects.all().order_by("-created_at")

    if category:
        if category not in VALID_CATEGORIES:
            raise Http404
        videos = videos.filter(category=category)

    return render(request, "media/videos.html", {
        "videos": videos,
        "categories": Category.choices,
        "current_category": category,
    })