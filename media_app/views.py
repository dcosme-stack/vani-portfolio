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

    seo = {
        "title": f"Vanishree Kulkarni – Photos",
        "description": "Learn more about Vanishree Kulkarni through her photos.",
        "image": request.build_absolute_uri("/static/images/og/og-photo.jpg"),
    }

    return render(request, "media/photos.html", {
        "photos": photos,
        "categories": Category.choices,
        "current_category": category,
        "seo": seo
    })


def video_list(request, category=None):
    videos = Video.objects.all().order_by("-created_at")

    if category:
        if category not in VALID_CATEGORIES:
            raise Http404
        videos = videos.filter(category=category)

    seo = {
        "title": f"Vanishree Kulkarni – Videos",
        "description": "Learn more about Vanishree Kulkarni through her videos.",
        "image": request.build_absolute_uri("/static/images/og/og-video.jpg"),
    }

    return render(request, "media/videos.html", {
        "videos": videos,
        "categories": Category.choices,
        "current_category": category,
        "seo":seo
    })