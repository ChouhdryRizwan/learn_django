from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home , name='Home'),
    path('projects/', views.ProjectPage , name='Projects'),
    path('categories/', views.Category , name='Categories'),
    path('details/<int:id>', views.DetailsPage , name='Details'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)