from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Photo, Video, Category



def photo_list(request, category_slug=None):
    photos = Photo.objects.select_related("category").filter(is_featured=True).order_by("-created_at")

    categories = Category.objects.filter(content_type="photo")

    current_category = None
    
    if category_slug:
        current_category = get_object_or_404(
            Category,
            slug=category_slug,
            content_type="photo",
        )
        photos = photos.filter(category=current_category)


    seo = {
        "title": f"Vanishree Kulkarni – Photos",
        "description": "Learn more about Vanishree Kulkarni through her photos.",
        "image": request.build_absolute_uri("/static/images/og/og-photo.jpg"),
    }

    return render(
        request,
        "media/photos.html",
        {
            "photos": photos,
            "categories": categories,
            "current_category": current_category,
            "seo": seo,
        }
    )


def video_list(request, category_slug=None):
    videos = Video.objects.select_related("category").filter(is_featured=True).order_by("-created_at")

    categories = Category.objects.filter(content_type="video")

    current_category = None

    if category_slug:
        current_category = get_object_or_404(
            Category,
            slug=category_slug,
            content_type="video",
        )
        videos = videos.filter(category=current_category)

    seo = {
        "title": "Vanishree Kulkarni – Videos",
        "description": "Learn more about Vanishree Kulkarni through her videos.",
        "image": request.build_absolute_uri("/static/images/og/og-video.jpg"),
    }

    return render(
        request,
        "media/videos.html",
        {
            "videos": videos,
            "categories": categories,
            "current_category": current_category,
            "seo":seo,
        }
    )