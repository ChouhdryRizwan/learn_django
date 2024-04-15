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

    py --version

`Unix/MacOS:`

    python --version

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