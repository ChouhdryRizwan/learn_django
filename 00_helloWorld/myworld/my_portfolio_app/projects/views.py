# def projects(request):
#     return HttpResponse("Hello world!")

from django.http import HttpResponse
from django.template import loader
from .models import *

def Home(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def ProjectPage(request):
  template = loader.get_template('projects.html')
  my_Project = Project.objects.all()
  project_Images = ProjectImage.objects.all()
  # context = {
  #   'projectname': 'NNjewellers',
  #   'greeting':1,
  # }
  context = {
    'projects': my_Project,
    'project_Images': project_Images,
    # 'projects': [
    #   {
    #     'name': 'NN Jewellers',
    #     'category': 'Web Designing',
    #     'link': 'https://nnjewelers.pk/'
    #   },{
    #     'name': 'Leather Crafted',
    #     'category': 'Web Development',
    #     'link': 'https://leathercrafted.store/'
    #   },{
    #     'name': 'Hiller Group',
    #     'category': 'Web Designing',
    #     'link': 'https://hillergroup.co.uk/'
    #   },
    #   ]
    }
  return HttpResponse(template.render(context,request))

def Category(request):
  template = loader.get_template('categories.html')
  categories = ProjectCategory.objects.all()
  context = {
    'categories': categories,
    # 'categories': ['Web Designing', 'Web Development', 'Graphic Designing'],   
  }
  return HttpResponse(template.render(context,request))