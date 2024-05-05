# Django Add Master Template
## The extends Tag


In the previous pages we created two templates, one for listing all members, and one for details about a member.

The templates have a set of HTML code that are the same for both templates.

Django provides a way of making a "parent template" that you can include in all pages to do the stuff that is the same in all pages.

Start by creating a template called `master.html`, with all the necessary HTML elements:

1. Create a file name `master.html` under the templates folder and paste this code:

        <!DOCTYPE html>
        <html>
        <head>
        <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
        {% include 'header.html' %}
        {% block content %}
        {% endblock %}

        {% include 'footer.html' %}

        </body>
        </html>

Do you see Django block Tag inside the `<title>` element, and the `<body>` element?

They are placeholders, telling Django to replace this block with content from other sources.

## Modify Templates

Now the three templates `(myfirst.html, projects.html, categories.html and details.html)` can use this master.html template.

This is done by including the master template with the `{% extends %}` tag, and inserting a title block and a content block:

2. Goto `myfirst.html` page and this code below:

        {% extends "master.html" %}

        {% block title %}
        Home - Projects
        {% endblock %}

        {% block content %}
        <h1>Home</h1>
        <p>Welcome to my first Django project!</p>

        {% with greeting=1 %}
        {% if greeting == 1 %}
        <h1>Hello</h1>
        {% else %}
        <h1>Bye</h1>
        {% endif %}
        {% endwith %}

        {% endblock %}

2. Goto `projects.html` page and this code below:

        {% extends "master.html" %}

        {% block title %}
        Portfolio - Projects
        {% endblock %}

        {% block content %}
        <h2>Our Projects</h2>

        {% for proj in projects %} 
        {% for img in project_Images %}
        <a href="/details/{{proj.id}}">
        {% if img.id == proj.id %}
        <img
                src="{% url 'Home' %}{{img.image}}"
                alt="{{img}}"
                height="100"
                width="auto"
        />
        <h4>{{ proj.title }}</h4>
        {% endif %} 
        </a>
        {% endfor %} 
        {% endfor %}

        {% endblock %}

3. Goto `categories.html` page and this code below:

        {% extends "master.html" %}

        {% block title %}
        Details - Projects
        {% endblock %}

        {% block content %}
        <h1>This is our Categories Page</h1>
        
        <h2>Our Experties in:</h2>
        <ul>
        {% for cat_name in categories %}
        <li>{{ cat_name }}</li>
        {% endfor %}
        </ul>
        {% endblock %}

4. Goto `details.html` page and this code below:       

{% extends "master.html" %}

        {% block title %}
        Details - Projects
        {% endblock %}

        {% block content %}

        <p>{{Project.category}}</p>
        <h1>{{ Project.title }}</h1>
        <img
                src="{% url 'Home' %}{{Image.image}}"
                alt="{{Image}}"
                height="100"
                width="auto"
        />
        <h5>{{ Project.description }}</h5>
        <a href="{{ Project.project_url }}" target="_blank">Visit</a>
        {% endblock %}

Now start the server:

    py manage.py runserver

In the browser window, type 127.0.0.1:8000/projects/ in the address bar.