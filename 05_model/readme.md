# Install Django

Now, that we have created a virtual environment, we are ready to install Django.

## Note: Remember to install Django while you are in the virtual environment!

`Django is installed using pip, with this command:`

`Windows:`

        (myworld) C:\Users\Your Name>py -m pip install Django

`Unix/MacOS:`

        (myworld) ... $ python -m pip install Django

`Which will give a result that looks like this (at least on my Windows machine):`

        Collecting Django
        Downloading Django-4.0.3-py3-none-any.whl (8.0 MB)
      |████████████████████████████████| 8.0 MB 2.2 MB/s
    Collecting sqlparse>=0.2.2
     Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
    Collecting asgiref<4,>=3.4.1
    Downloading asgiref-3.5.0-py3-none-any.whl (22 kB)
    Collecting tzdata; sys_platform == "win32"
    Downloading tzdata-2021.5-py2.py3-none-any.whl (339 kB)
      |████████████████████████████████| 339 kB 6.4 MB/s
    Installing collected packages: sqlparse, asgiref, tzdata, Django
    Successfully installed Django-4.0.3 asgiref-3.5.0 sqlparse-0.4.2 tzdata-2021.5

` That's it! Now you have installed Django in your new project, running in a virtual environment!`

## Windows, Mac, or Unix?

You can run this project on either one. There are some small differences, like when writing commands in the command prompt, Windows uses py as the first word in the command line, while Unix and MacOS use python:

`Windows:`

    django-admin --version

`Unix/MacOS:`

    django-admin --version

`In the rest of this tutorial, we will be using the Windows command.`

## Check Django Version

If Django is installed, you will get a result with the version number:

        5.0.4

# Django Create Project

## My First Project

Once you have come up with a suitable name for your Django project, like mine:
`my_portfolio_app`, navigate to where in the file system you want to store the code (in the virtual environment), I will navigate to the myworld folder, and run this command in the command prompt:

        django-admin startproject my_portfolio_app

Django creates a my_portfolio_app folder on my computer, with this content:

        my_portfolio_app
        manage.py
    my_portfolio_app/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py

These are all files and folders with a specific meaning, you will learn about some of them later in this tutorial, but for now, it is more important to know that this is the location of your project, and that you can start building applications in it.

## Run the Django Project

Now that you have a Django project, you can run it, and see what it looks like in a browser.

Navigate to the `/my_portfolio_app` folder and execute this command in the command prompt:

        py manage.py runserver

Which will produce this result:

    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    April 15, 2024 - 10:53:30
    Django version 5.0.4, using settings 'my_portfolio_app.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

`Open a new browser window and type 127.0.0.1:8000 in the address bar.`

## Django Apps

In the Django philosophy we have two important concepts:

`app:` is a Web application that does something. An app usually is composed of a set of models (database tables), views, templates, tests.

`project:` is a collection of configurations and apps. One project can be composed of multiple apps, or a single app.

It’s important to note that you can’t run a Django app without a project. Simple websites like a blog can be written entirely inside a single app, which could be named blog or weblog for example.

# Django Create App

## What is an App?

An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a projects database.

In this tutorial we will create an app that allows us to list and register projects in a database.

But first, let's just create a simple Django app that displays "Hello World!".

## Create App

I will name my app `projects.`

Start by navigating to the selected location where you want to store the app, in my case the `my_portfolio_app` folder, and run the command below.

`If the server is still running, and you are not able to write commands, press [CTRL] [BREAK], or [CTRL] [C] to stop the server and you should be back in the virtual environment.`

        py manage.py startapp projects

Django creates a folder named projects in my project, with this content:

        my_portfolio_app
             manage.py
             my_portfolio_app/
             project/
                migrations/
                      __init__.py
                __init__.py
                admin.py
                apps.py
                models.py
                tests.py
                views.py

These are all files and folders with a specific meaning. You will learn about most of them later in this tutorial.

First, take a look at the file called `views.py.`

This is where we gather the information we need to send back a proper response.

## Django Views

# Views

Django views are Python functions that takes http requests and returns http response, like HTML documents.

A web page that uses Django is full of views with different tasks and missions.

Views are usually put in a file called `views.py` located on your app's folder.

There is a `views.py` in your `project` folder that looks like this:

`my_portfolio_app/project/views.py:`

        from django.shortcuts import render
        # Create your views here.

Find it and open it, and replace the content with this:

`my_portfolio_app/project/views.py:`

        from django.shortcuts import render
        from django.http import HttpResponse

        def project(request):
        return HttpResponse("Hello world!")

`Note:` The name of the view does not have to be the same as the application.

I call it `project` because I think it fits well in this context.

This is a simple example on how to send a response back to the browser.

But how can we execute the view? Well, we must call the view via a URL.

## Django URLs

# URLs

Create a file named `urls.py` in the same folder as the `views.py` file, and type this code in it:

my_portfolio_app/project/urls.py:

        from django.urls import path
        from . import views

        urlpatterns = [
         path('projects/', views.project, name='projects'),
        ]

The `urls.py` file you just created is specific for the `projects` application. We have to do some routing in the root directory `my_portfolio_app` as well. This may seem complicated, but for now, just follow the instructions below.

There is a file called `urls.py` on the my_portfolio_app folder, open that file and add the `include` module in the `import` statement, and also add a `path()` function in the `urlpatterns[]` list, with arguments that will route users that comes in via `127.0.0.1:8000/.`

my_portfolio_app/my_portfolio_app/urls.py:

        from django.contrib import admin
        from django.urls import include, path

        urlpatterns = [
        path('', include('projects.urls')),
        path('admin/', admin.site.urls),
        ]

If the server is not running, navigate to the `/my_portfolio_app` folder and execute this command in the command prompt:

        py manage.py runserver

In the browser window, type `127.0.0.1:8000/projects/` in the address bar.

## Django Templates

# Templates

In the `Django Intro` page, we learned that the result should be in HTML, and it should be created in a template, so let's do that.

Create a `templates` folder inside the `projects` folder, and create a HTML file named `myfirst.html`.

The file structure should be like this:

        my_portfolio_app
         manage.py
         my_portfolio_app/
         projects/
            templates/
               myfirst.html

Open the HTML file and insert the following:

`my_portfolio_app/projects/templates/myfirst.html:`

## Modify the View

Open the `views.py` file and replace the `projects` view with this:

my_portfolio_app/projects/views.py:

        from django.http import HttpResponse
        from django.template import loader

        def projects(request):
         template = loader.get_template('myfirst.html')
         return HttpResponse(template.render())

## Change Settings

To be able to work with more complicated stuff than "Hello World!", We have to tell Django that a new app is created.

This is done in the `settings.py` file in the `my_portfolio_app` folder.

Look up the `INSTALLED_APPS[]` list and add the `projects` app like this:

my_portfolio_app/my_portfolio_app/settings.py:

        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'projects'
        ]

`Then run this command:`

        py manage.py migrate

Which will produce this output:

        Operations to perform:
        Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying auth.0001_initial... OK
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying admin.0003_logentry_add_action_flag_choices... OK
        Applying contenttypes.0002_remove_content_type_name... OK
        Applying auth.0002_alter_permission_name_max_length... OK
        Applying auth.0003_alter_user_email_max_length... OK
        Applying auth.0004_alter_user_username_opts... OK
        Applying auth.0005_alter_user_last_login_null... OK
        Applying auth.0006_require_contenttypes_0002... OK
        Applying auth.0007_alter_validators_add_error_messages... OK
        Applying auth.0008_alter_user_username_max_length... OK
        Applying auth.0009_alter_user_last_name_max_length... OK
        Applying auth.0010_alter_group_name_max_length... OK
        Applying auth.0011_update_proxy_permissions... OK
        Applying auth.0012_alter_user_first_name_max_length... OK
        Applying sessions.0001_initial... OK

Start the server by navigating to the `/my_portfolio_app` folder and execute this command:

In the browser window, type `127.0.0.1:8000/projects/` in the address bar.

## Django Models

A Django model is a table in your database.

# Django Models

Up until now in this tutorial, output has been static data from Python or HTML templates.

Now we will see how Django allows us to work with data, without having to change or upload files in the prosess.

In Django, data is created in objects, called Models, and is actually tables in a database.

## Create Table (Model)

To create a model, navigate to the `models.py` file in the `/projects/` folder.

Open it, and add a `Project` table by creating a `Project class`, and describe the table fields in it:

        class Project(models.Model):
        projectname = models.CharField(max_length=255)
        projectcategory = models.CharField(max_length=255)

The first field, projectname, is a Text field, and will contain the project name of the projects.

The second field, projectcategory, is also a Text field, with the project category name.

Both projectname and projectcategory is set up to have a maximum of 255 characters.

## SQLite Database

When we created the Django project, we got an empty SQLite database.

It was created in the my_portfolio_app root folder, and has the filename db.sqlite3.

By default, all Models created in the Django project will be created as tables in this database.

# Migrate

Now when we have described a Model in the `models.py` file, we must run a command to actually create the table in the database.

Navigate to the /my_portfolio_app/ folder and run this command:

        py manage.py makemigrations projects

Which will result in this output:

        Migrations for 'projects':
        projects\migrations\0001_initial.py
        - Create model Project

        (myworld) D:\Learn Django\learn_django\00_helloWorld\myworld\my_portfolio_app>

Django creates a file describing the changes and stores the file in the /migrations/ folder:

        # Generated by Django 5.0.4 on 2024-04-16 19:36

        from django.db import migrations, models


        class Migration(migrations.Migration):

        initial = True

        dependencies = [
        ]

        operations = [
                migrations.CreateModel(
                name='Project',
                fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('projectname', models.CharField(max_length=255)),
                        ('projectcategory', models.CharField(max_length=255)),
                ],
                ),
        ]


Note that Django inserts an id field for your tables, which is an auto increment number (first record gets the value 1, the second record 2 etc.), this is the default behavior of Django, you can override it by describing your own id field.

The table is not created yet, you will have to run one more command, then Django will create and execute an SQL statement, based on the content of the new file in the /migrations/ folder.

Run the migrate command:

        py manage.py migrate

Which will result in this output:

        Operations to perform:
        Apply all migrations: admin, auth, contenttypes, projects, sessions
        Running migrations:
        Applying projects.0001_initial... OK

        (myworld) D:\Learn Django\learn_django\00_helloWorld\myworld\my_portfolio_app>

`Now you have a Project table in you database!`    

# View SQL

As a side-note: you can view the SQL statement that were executed from the migration above. All you have to do is to run this command, with the migration number:

        py manage.py sqlmigrate projects 0001

Which will result in this output:

        BEGIN;
        --
        -- Create model Project
        --
        CREATE TABLE "projects_project" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "projectname" varchar(255) NOT NULL, "projectcategory" varchar(255) NOT NULL);
        COMMIT;

        (myworld) D:\Learn Django\learn_django\00_helloWorld\myworld\my_portfolio_app>

# Django Insert Data
## Add Records

The Projects table created in the previous code is empty.

We will use the Python interpreter (Python shell) to add some members to it.

`To open a Python shell, type this command:`

        py manage.py shell


`Now we are in the shell, the result should be something like this:`        

        Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        (InteractiveConsole)
        >>>

`At the bottom, after the three >>> write the following:`   

        from projects.models import Project

`Hit [enter] and write this to look at the empty Project table:`

        Project.objects.all()

`This should give you an empty QuerySet object, like this:`

        <QuerySet []>

A QuerySet is a collection of data from a database.

Read more about QuerySets in latter chapter.

Add a record to the table, by executing these two lines:        

        project = Project(projectname='firstproject', projectcategory='firstcategory')
        project.save()

`Execute this command to see if the Member table got a member:`

        Project.objects.all().values()

`Hopefully, the result will look like this:`

                <QuerySet [{'id': 1, 'projectname': 'firstproject', 'projectcategory': 'firstcategory'}]>


# Django Update Model
## Add Fields in the Model

`To add a field to a table after it is created, open the models.py file, and make your changes:`

my_portfolio_app/projects/models.py:

        from django.db import models

        class Project(models.Model):
        projectname = models.CharField(max_length=255)
        projectcategory = models.CharField(max_length=255)
        project_image = models.ImageField(),
        project_date = models.DateField(),

As you can see, we want to add Project Image and Project Date to our Project Model.

This is a change in the Model's structure, and therefor we have to make a migration to tell Django that it has to update the database:        

        py manage.py makemigrations projects


Which, in my case, will result in a prompt, because I try to add fields that are not allowed to be null, to a table that already contains records.

As you can see, Django asks if I want to provide the fields with a specific value, or if I want to stop the migration and fix it in the model:        

        py manage.py makemigrations projects
        You are trying to add a non-nullable field 'project_date' to projects without a default; we can't do that (the database needs something to populate existing rows).
        Please select a fix:
        1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
        2) Quit, and let me add a default in models.py
        Select an option:


I will select option 2, and open the models.py file again and allow NULL values for the two new fields:

my_portfolio_app/projects/models.py:

        from django.db import models

        class Project(models.Model):
        projectname = models.CharField(max_length=255)
        projectcategory = models.CharField(max_length=255)
        project_image = models.ImageField(null=True),
        project_date = models.DateField(null=True),

`And make the migration once again:`
        
        py manage.py makemigrations projects

Which will result in this:

                Migrations for 'projects':
  projects\migrations\0002_project_project_image_project_date.py
    - Add field project_image to project
    - Add field project_date to project   

`Run the migrate command:`

        py manage.py migrate

`Which will result in this output:`        

        ...

## Insert Data        