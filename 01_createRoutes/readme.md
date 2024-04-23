# Create Multiple Routes

` First of all you have to navigate to the templates folder that we create in our previous example in app (projects) folder.`

1. Create a file `projects.html` and under the templates folder and paste this code:

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Projects</title>
        </head>
        <body>
            <h1>This is our Project Page</h1>
        </body>
        </html>

2. Create another file `categories.html` and under the templates folder and paste this code:

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Categories</title>
        </head>
        <body>
            <h1>This is our Categories Page</h1>
        </body>
        </html>

3. Now we have to render templates file in `views.py` file that is located in under app (projects) folder and paste this code:


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

4. Register the newely created views in URLs, this file (`urls.py`) is located in under the app (projects) folder and paste this code:

        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.Home , name='Home'),
            path('projects/', views.Project , name='projects'),
            path('categories/', views.Category , name='categories'),
            
        ]

## Note: Your routes are set wit a default home page that we created from previous example name `myfirst.html`.

If the server is not running, navigate to the /my_portfolio_app folder and execute this command in the command prompt:

        py manage.py runserver

In the browser window, type 127.0.0.1:8000/projects/ in the address bar.        