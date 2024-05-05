# Details
## Add some deatils and settings so the project get better.

1. First of all set `projects.html` page and replace code with this code:

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Projects</title>
        </head>
        <body>
            <a href="/">Home</a> &nbsp;&nbsp; <a href="/categories">Categories</a>
            <br />

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
            </a>
            {% endif %} {% endfor %} {% endfor %}
        </body>
        </html>


2. Add a `details.html` page under the templates folder and paste the code below:

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Details</title>
        </head>
        <body>
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
        </body>
        </html>


3. Create a function in `views.py` for details page and paste this code:

        def DetailsPage(request, id):
        ProjectDetails = Project.objects.get(id = id)
        Image = ProjectImage.objects.get(id = id)
        template = loader.get_template('details.html')
        context = {
            'Project': ProjectDetails,
            'Image': Image,
        }
        return HttpResponse(template.render(context,request))

4. Goto `urls.py` file under the `projects` folder, and add this code in urlpatterns:

        path('details/<int:id>', views.DetailsPage , name='Details'),

Now start the server:

    py manage.py runserver

In the browser window, type 127.0.0.1:8000/projects/ in the address bar.        