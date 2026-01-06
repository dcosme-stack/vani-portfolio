from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Homepage, About_Vani, Article, Resume, Skill, Reference, Experience
# Create your views here.


def home_view(request):
  homepage = Homepage.objects.first()
  template = loader.get_template('pages/homepage.html')
  context = {
    'homepage':homepage,
    }

  return HttpResponse(template.render(context, request))

def about_view(request):
  about = About_Vani.objects.prefetch_related("articles").first()
  template = loader.get_template('pages/about.html')
  context = {
    'about': about,
    }

  return HttpResponse(template.render(context, request))

def resume_view(request):
  resume = Resume.objects.prefetch_related(
        "skills",
        "experiences",
        "references",
    ).first()
  template = loader.get_template('pages/resume.html')
  context = {
    'resume': resume,
    }

  return HttpResponse(template.render(context, request))