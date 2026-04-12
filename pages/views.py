from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Homepage, Showreel, About_Vani, Resume, Credits, Credits_Category
# Create your views here.


def home_view(request):
  homepage = Homepage.objects.prefetch_related("articles").first()
  seo = {
        "title": f"Vanishree Kulkarni – Homepage",
        "description": "Welcome to Vanishree Kulkarni portfolio website.",
        "image": request.build_absolute_uri("/static/images/og/og-homepage.jpg"),
    }
  template = loader.get_template('pages/homepage.html')
  context = {
    'homepage':homepage,
    "seo": seo
    }

  return HttpResponse(template.render(context, request))

def showreel_view(request):
  showreel = Showreel.objects.first()
  seo = {
        "title": f"Vanishree Kulkarni – Showreel",
        "description": "Welcome to Vanishree Kulkarni portfolio website.",
        "image": request.build_absolute_uri("/static/images/og/og-homepage.jpg"),
    }
  template = loader.get_template('pages/showreel.html')
  context = {
    'showreel':showreel,
    "seo": seo
    }

  return HttpResponse(template.render(context, request))


def credits_view(request, category_slug=None):
  credits = Credits.objects.prefetch_related("category").all().order_by('category', '-date')

  categories = Credits_Category.objects.all()

  current_category = None
    
  if category_slug:
      current_category = get_object_or_404(
          Credits_Category,
          slug=category_slug,
      )
      credits = credits.filter(category=current_category)

  seo = {
        "title": f"Vanishree Kulkarni – Credits",
        "description": "Learn more about Vanishree Kulkarni experiences and filmography.",
        "image": request.build_absolute_uri("/static/images/og/og-resume.jpg"),
    }
  template = loader.get_template('pages/credits.html')
  context = {
    'credits': credits,
    "seo": seo,
    "categories": categories,
    "current_category": current_category,
    }

  return HttpResponse(template.render(context, request))


def about_view(request):
  about = About_Vani.objects.prefetch_related("articles_bkp").first()
  seo = {
        "title": f"Vanishree Kulkarni – About",
        "description": "Learn more about Vanishree Kulkarni, her biography, and career highlights.",
        "image": request.build_absolute_uri("/static/images/og/og-about.jpg"),
    }
  template = loader.get_template('pages/about.html')
  context = {
    'about': about,
    "seo": seo
    }

  return HttpResponse(template.render(context, request))

def resume_view(request):
  resume = Resume.objects.prefetch_related(
        "skills",
        "languages",
        "experiences",
        "references",
    ).first()
  seo = {
        "title": f"Vanishree Kulkarni – Resume",
        "description": "Learn more about Vanishree Kulkarni experiences and filmography.",
        "image": request.build_absolute_uri("/static/images/og/og-resume.jpg"),
    }
  template = loader.get_template('pages/resume.html')
  context = {
    'resume': resume,
    "seo": seo
    }

  return HttpResponse(template.render(context, request))