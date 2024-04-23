# Django Admin - Include Project
## Include Project in the Admin Interface

To include the Project model in the admin interface, we have to tell Django that this model should be visible in the admin interface.

This is done in a file called admin.py, and is located in your app's folder, which in our case is the projects folder.

Open it, and it should look like this:

`my_portfolio_app/projects/admin.py:`

from django.contrib import admin

# Register your models here.

Insert a couple of lines here to make the Project model visible in the admin page:

    from django.contrib import admin
    from . models import ProjectCategory, Project, ProjectImage

    admin.site.register(ProjectCategory)
    admin.site.register(Project)
    admin.site.register(ProjectImage)

Now start the server:

    py manage.py runserver

In the browser window, type 127.0.0.1:8000/admin/ in the address bar.

`You will see these all tables (e.g) models in admin panel.`

Now, Insert `Category`, `Project` and `Project Images`.