from django.db import models

class ProjectCategory(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_url = models.URLField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('ProjectCategory', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title    

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project_images/')
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Image for {self.project.title}"
