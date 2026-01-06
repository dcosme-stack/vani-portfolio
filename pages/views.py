from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Homepage, About_Vani, Article, Resume, Skill, Reference, Experience
# Create your views here.


def home_view(request):
  myhomepage = Homepage.objects.first()
  template = loader.get_template('pages/home.html')
  context = {
    'myhomepage':myhomepage,
    }

  return HttpResponse(template.render(context, request))

def about_view(request):
  myabout = About_Vani.objects.first()
  myarticles = Article.objects.all()
  template = loader.get_template('pages/about.html')
  context = {
    'myabout': myabout,
    'myarticles': myarticles,
    }

  return HttpResponse(template.render(context, request))

def resume_view(request):
  myresume = Resume.objects.first()
  myskills = Skill.objects.all()
  myreferences = Reference.objects.all()
  myexperiences = Experience.objects.all()
  template = loader.get_template('pages/resume.html')
  context = {
    'myresume': myresume,
    'myskills': myskills,
    'myreferences': myreferences,
    'myexperiences': myexperiences,
    }

  return HttpResponse(template.render(context, request))