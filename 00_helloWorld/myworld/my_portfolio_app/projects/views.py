# from django.shortcuts import render
# from django.http import HttpResponse

# def projects(request):
#     return HttpResponse("Hello world!")

from django.http import HttpResponse
from django.template import loader

def projects(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())