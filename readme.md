# Let's Learn Django

## Learn Python is mandatory before starting django.

[Or Follow this guide](https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html)

# Introduction

## What is Django?

1. Django is a Python framework that makes it easier to create web sites using Python.

2. Django takes care of the difficult stuff so that you can concentrate on building your web applications.

3. Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).

# Django History

Django was invented by Lawrence Journal-World in 2003, to meet the short deadlines in the newspaper and at the same time meeting the demands of experienced web developers.

Initial release to the public was in July 2005.

Latest version of Django is 5.0.4 (August 2024).

# How does Django Work?

* Django follows the MVT design pattern (Model View Template).

`Model` - The data you want to present, usually data from a database.

`View` - A request handler that returns the relevant template and content - based on the request from the user.

`Template` - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

## Model

The model provides data from the database.

In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases.

The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it.

Django, with ORM, makes it easier to communicate with the database, without having to write complex SQL statements.

The models are usually located in a file called models.py.

## View

A view is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the final result.

The views are usually located in a file called views.py.

## Template

A template is a file where you describe how the result should be represented.

Templates are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other results, but we will concentrate on .html files.

Django uses standard HTML to describe the layout, but uses Django tags to add logic:

    <h1>My Homepage</h1>

    <p>My name is {{ firstname }}.</p>

The templates of an application is located in a folder named templates.

# URLs

Django also provides a way to navigate around the different pages in a website.

When a user requests a URL, Django decides which view it will send it to.

This is done in a file called urls.py.


## Behind the scene

When you have installed Django and created your first Django web application, and the browser requests the URL, this is basically what happens:


* Django receives the URL, checks the urls.py file, and calls the view that matches the URL.
* The view, located in views.py, checks for relevant models.
* The models are imported from the models.py file.
* The view then sends the data to a specified template in the template folder.
* The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.

# Getting Started

* To install Django, you must have [Python](https://www.python.org/downloads) installed, and a package manager like PIP.

* PIP is included in Python from version 3.4.

## Django Requires Python
* To check if your system has Python installed, run this command in the command prompt:

        python --version

* If Python is installed, you will get a result with the version number, like this

        Python 3.9.2

* If you find that you do not have Python installed on your computer, then you can download it for free from the following website:  [Download Python](https://www.python.org/) 


# PIP

* To install Django, you must use a package manager like PIP, which is included in Python from version 3.4.

* To check if your system has PIP installed, run this command in the command prompt:

        pip --version

* If PIP is installed, you will get a result with the version number.

* For me, on a windows machine, the result looks like this:

        pip 23.2.1 from C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)

* If you do not have PIP installed, you can download and install it from this page:
[Download Pip](https://pypi.org/project/pip) 


# Django - Create Virtual Environment

## Virtual Environment

* It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv, which is included in Python.

* The name of the virtual environment is your choice, in this tutorial we will call it `myworld`.

* Type the following in the command prompt, remember to navigate to where you want to create your project:


`Windows:` 

    (myworld) C:\Users\Your Name>

`Unix/MacOS:`    

    (myworld) ... $

`Note:`

*  This will set up a virtual environment, and create a folder named "myworld" with subfolders and files, like this:

        myworld
          Include
          Lib
          Scripts
          pyvenv.cfg

* Then you have to activate the environment, by typing this command:

`Windows:`
        
        myworld\Scripts\activate.bat

`Unix/MacOS:`
        
        source myworld/bin/activate

* Once the environment is activated, you will see this result in the command prompt:        

`Windows:`
        
        (myworld) C:\Users\Your Name>

`Unix/MacOS:`
        
       (myworld) ... $


`Note:` You must activate the virtual environment every time you open the command prompt to work on your project.       