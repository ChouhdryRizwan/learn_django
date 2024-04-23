# Send Data
## Now we send data from view to templates and perfrom logical operations.

# Django Template Variables

In Django templates, you can render variables by putting them inside `{{ }}` brackets:

`for example:`

    <h1>Hello {{ firstname }}, how are you?</h1>

## Create Variable in View

The variable firstname in the example above was sent to the template via a view:

1. First of all you have to navigate to the `views.py` under the app (`projects`) folder and update the `Project` function:

        def Project(request):
        template = loader.get_template('projects.html')
        context = {
            'projectname': 'NNjewellers',
        }
        return HttpResponse(template.render(context,request))

2. Now we have to naviagte `templates` folder under the app (projects) folder.
3. After navigate to this folder open file `projects.html` and paste this code:

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Projects</title>
        </head>
        <body>
            <h1>This is our Project Page</h1>
            <a href="/">Home</a> &nbsp;&nbsp;
            <a href="/categories">Categories</a> <br>
            <h2>Our 1st Project Name is  {{ projectname }}.</h2>
        </body>
</html>

`As you can see in the view above, we create an object named context and fill it with data, and send it as the first parameter in the template.render() function.`

If the server is not running, navigate to the /my_portfolio_app folder and execute this command in the command prompt:

    py manage.py runserver

In the browser window, type 127.0.0.1:8000/projects/ in the address bar.    

You can also craete variables in template file.

## Create Variables in Template

You can also create variables directly in the template, by using the `{% with %}` template tag.

The variable is available until the `{% endwith %}` tag appears:

`for example:`

    {% with projectname="NNjewellers" %}
    <h2>Our 1st Project Name is  {{ projectname }}.</h2>
    {% endwith %}

# Django Template Tags

In Django templates, you can perform programming logic like executing `if` statements and `for` loops.

These keywords, `if` and `for`, are called "template tags" in Django.

To execute template tags, we surround them in `{% %}` brackets.

`for example:`

    {% with greeting=1 %}
    {% if greeting == 1 %}
    <h1>Hello</h1>
    {% else %}
    <h1>Bye</h1>
    {% endif %}
    {% endwith %}

## Django comment Tag

Comments: Allows you to have sections of code that should be ignored.

`for example:`

    <h1>Welcome Everyone</h1>
    {% comment %}
    <h1>Welcome ladies and gentlemen</h1>
    {% endcomment %}

`Comment Description`

You can add a message to your comment, to help you remember why you wrote the comment, or as message to other people reading the code.

`for example:`

        <h1>Welcome Everyone</h1>
        {% comment "this was the original welcome message" %}
            <h1>Welcome ladies and gentlemen</h1>
        {% endcomment %}`

`Smaller Comments`

You can also use the {# ... #} tags when commenting out code, which can be easier for smaller comments:

`for example:`

    <h1>Welcome{# Everyone#}</h1>

`Comment in Views`

Views are written in Python, and Python comments are written with the `#` character:

`for example:`

    def Project(request):
    template = loader.get_template('projects.html')
    # context = {
    #   'projectname': 'NNjewellers',
    #   'greeting':1,
    # }
    context = {
        'projects': [
        {
            'name': 'NN Jewellers',
            'category': 'Web Designing',
            'link': 'https://nnjewelers.pk/'
        },{
            'name': 'Leather Crafted',
            'category': 'Web Development',
            'link': 'https://leathercrafted.store/'
        },{
            'name': 'Hiller Group',
            'category': 'Web Designing',
            'link': 'https://hillergroup.co.uk/'
        },
        ]
        }
    return HttpResponse(template.render(context,request))


## Django if Tag

1. If Statement

An `if` statement evaluates a variable and executes a block of code if the value is true.

Naviagte to the `views.py` file and update Project function:

    def Project(request):
    template = loader.get_template('projects.html')
    context = {
        'projectname': 'NNjewellers',
        'greeting':1,
    }
    return HttpResponse(template.render(context,request))

Navigate to the `projects.html` under the templates folder in our app (`project`) directory and paste code:

     {% if greeting == 1 %}
    <h1>Hello</h1>
    {% else %}
    <h1>Bye</h1>
    {% endif %}

If the server is not running, navigate to the /my_portfolio_app folder and execute this command in the command prompt:

    py manage.py runserver

In the browser window, type 127.0.0.1:8000/projects/ in the address bar.    

2. Elif

The `elif` keyword says "if the previous conditions were not true, then try this condition".


`for exmaple:`

    {% if greeting == 1 %}
    <h1>Hello</h1>
    {% elif greeting == 2 %}
    <h1>Welcome</h1>
    {% endif %} 

3. Else
    
The else keyword catches anything which isn't caught by the preceding conditions.

`for example:`

    {% if greeting == 1 %}
    <h1>Hello</h1>
    {% elif greeting == 2 %}
    <h1>Welcome</h1>
    {% else %}
    <h1>Goodbye</h1>
    {% endif %} 

## Django Operators

The above examples uses the == operator, which is used to check if a variable is equal to a value, but there are many other operators you can use, or you can even drop the operator if you just want to check if a variable is not empty:

`for example:`

    {% if greeting %}
    <h1>Hello</h1>
    {% endif %} 

1. `==` Is equal to.

`for example:`

    {% if greeting == 2 %}
    <h1>Hello</h1>
    {% endif %} 

2. `!=` Is not equal to.

`for example:`

    {% if greeting != 1 %}
    <h1>Hello</h1>
    {% endif %} 

## Other Operators.

3. `<=` Is less than, or equal to.
4. `>` Is greater than.
5. `>=` Is greater than, or equal to.
6. `and`
7. `or`
8. `and/or`
9. `in`
10. `not in`
11. `is`
12. `is not`


## Django for Tag

1. For Loops

A `for` loop is used for iterating over a sequence, like looping over items in an array, a list, or a dictionary.

`for example:`

    {% for x in projects %}
    <h1>{{ x }}</h1>
    {% endfor %}


Navigate to the `views.py` under the app (`projects`) folder and update the `Project` function:

    template = loader.get_template('categories.html')
    context = {
        'categories': ['Web Designing', 'Web Development', 'Graphic Designing'],   
    }
    return HttpResponse(template.render(context,request))

2. Now we have to naviagte `templates` folder under the app (projects) folder.
3. After navigate to this folder open file `categories.html.` and paste this code:

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Categories</title>
        </head>
        <body>
            <h1>This is our Categories Page</h1>
            <a href="/">Home</a> &nbsp;&nbsp; <a href="/projects">Project</a> <br />

            <h2>Our Experties in:</h2>
            <ul>
            {% for cat_name in categories %}
            <li>{{ cat_name }}</li>
            {% endfor %}
            </ul>
        </body>
        </html>

If the server is not running, navigate to the /my_portfolio_app folder and execute this command in the command prompt:

    py manage.py runserver

In the browser window, type 127.0.0.1:8000/projects/ in the address bar. 

## Loop through a list of dictionaries:

1. Naviagte to the `views.py` file and update Project function:

        def Project(request):
        template = loader.get_template('projects.html')
        `#` context = {
        `#`   'projectname': 'NNjewellers',
        `#`   'greeting':1,
        `#` }
        context = {
            'projects': [
            {
                'name': 'NN Jewellers',
                'category': 'Web Designing',
                'link': 'https://nnjewelers.pk/'
            },{
                'name': 'Leather Crafted',
                'category': 'Web Development',
                'link': 'https://leathercrafted.store/'
            },{
                'name': 'Hiller Group',
                'category': 'Web Designing',
                'link': 'https://hillergroup.co.uk/'
            },
            ]
            }
        return HttpResponse(template.render(context,request))


2. Navigate to the `projects.html` under the templates folder in our app (`project`) directory and paste code:

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
            <h3>{{ proj.name }}</h3>
            <p>{{ proj.category }}</p>
            <a href="{{ proj.link }}" target="_blank">Visit</a>
            {% endfor %}
        </body>
        </html>