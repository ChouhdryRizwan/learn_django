# Django include Tag
## Include

The include tag allows you to include a template inside the current template.

This is useful when you have a block of content that is the same for many pages.`

1. Create a file `header.html` under the template folder and paste this code:

        <p>This is Header</p>

2. Create a file `footer.html` under the template folder and paste this code:

        <p>This is Footer</p>

3. Add these lines of code where you want to show header and footer:

`for header:`

    {% include 'header.html' %}

`for footer:`      

    {% include 'footer.html' %}
