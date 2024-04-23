# def projects(request):
#     return HttpResponse("Hello world!")

from django.http import HttpResponse
from django.template import loader

def Home(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def Project(request):
  template = loader.get_template('projects.html')
  return HttpResponse(template.render())

def Category(request):
  template = loader.get_template('categories.html')
  return HttpResponse(template.render())