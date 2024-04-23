from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home , name='Home'),
    path('projects/', views.Project , name='projects'),
    path('categories/', views.Category , name='categories'),
    
]