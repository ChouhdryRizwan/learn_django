# View Data

Next we need to make the model data available in the template. This is done in the view.

In the view we have to import the Project model, and send it to the template like this:

`my_portfolio_app/projects/views.py:`

1. Import this statment at the top of the file.

    from .models import *

It will import all models from model file.

2. Now you have to update the `Category` function and paste this code:

        def Category(request):
        template = loader.get_template('categories.html')
        categories = ProjectCategory.objects.all()
        context = {
            'categories': categories,
            # 'categories': ['Web Designing', 'Web Development', 'Graphic Designing'],   
        }
        return HttpResponse(template.render(context,request))
        
All done, now run the server and visit the category page, you will see the categories but for this time categories show from table dynamically.

Now start the server:

    py manage.py runserver

In the browser window, type 127.0.0.1:8000/categories/ in the address bar.

2. Now you have to update the `ProjectPage` function and paste this code:

        def ProjectPage(request):
        template = loader.get_template('projects.html')
        my_Project = Project.objects.all()
        project_Images = ProjectImage.objects.all()
        `#` context = {
        `#`   'projectname': 'NNjewellers',
        `#`   'greeting':1,
        `#` }
        context = {
            'projects': my_Project,
            'project_Images': project_Images,
            `#` 'projects': [
            `#`   {
            `#`     'name': 'NN Jewellers',
            `#`     'category': 'Web Designing',
            `#`     'link': 'https://nnjewelers.pk/'
            `#`   },{
            `#`     'name': 'Leather Crafted',
            `#`     'category': 'Web Development',
            `#`     'link': 'https://leathercrafted.store/'
            `#`   },{
            `#`     'name': 'Hiller Group',
            `#`     'category': 'Web Designing',
            `#`     'link': 'https://hillergroup.co.uk/'
            `#`   },
            `#`   ]
            }
        return HttpResponse(template.render(context,request))

4. You also have to update the `urls.py` file located in project `app` folder and paste this code.

    from django.urls import path
    from . import views

        urlpatterns = [
            path('', views.Home , name='Home'),
            path('projects/', views.ProjectPage , name='projects'),
            path('categories/', views.Category , name='categories'),
        ]

5. Update the `projects.html` under the project `app` folder and paste this code.

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Projects</title>
        </head>
        <body>
            <h1>This is our Project Page</h1>
            <a href="/">Home</a> &nbsp;&nbsp; <a href="/categories">Categories</a>
            <br />
            <h2>Our 1st Project Name is {{ projectname }}.</h2>

            {% if greeting == 1 %}
            <h1>Hello</h1>
            {% endif %}
            <br />

            <h2>Our Portfolio</h2>
            {% for proj in projects %}
            <h3>{{ proj.title }}</h3>
            <h4>{{ proj.category }}</h4>
            <p>{{ proj.description }}</p>
            <p>{{ proj.date_created }}</p>
            <a href="{{ proj.project_url }}" target="_blank">Visit</a>
            {% endfor %}
            
            {% for img in project_Images %}
            <p>{{ img.image }}</p>
            {% endfor %}
        </body>
        </html>

Now start the server:

    py manage.py runserver

In the browser window, type 127.0.0.1:8000/projects/ in the address bar.
