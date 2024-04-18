from django.db import models

class Project(models.Model):
  projectname = models.CharField(max_length=255)
  projectcategory = models.CharField(max_length=255)
  project_date = models.DateField(),
  project_image = models.ImageField(),
