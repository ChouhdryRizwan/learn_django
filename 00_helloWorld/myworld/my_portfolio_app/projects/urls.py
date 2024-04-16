from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects , name='projects'),
]


# from django.http import HttpResponse
# from django.template import loader

# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())