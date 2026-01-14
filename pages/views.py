from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Homepage, About_Vani, Article, Resume, Skill, Reference, Experience
# Create your views here.


def home_view(request):
  homepage = Homepage.objects.first()
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

def about_view(request):
  about = About_Vani.objects.prefetch_related("articles").first()
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