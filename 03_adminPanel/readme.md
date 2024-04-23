# Django Admin
## Create User

To be able to log into the admin application, we need to create a user.

This is done by typing this command in the command view:

        py manage.py createsuperuser

Which will give this prompt:

    Username (leave blank to use 'dell'):

Here you must enter: username, e-mail address, (you can just pick a fake e-mail address), and password:

    Username (leave blank to use 'dell'): admin
    Email address: muhammadrizwantahir23@gmail.com
    Password:
    Password (again):
    The password is too similar to the username.
    This password is too short. It must contain at least 8 characters.
    This password is too common.
    Bypass password validation and create user anyway? [y/N]: N
    Password:
    Password (again):
    The password is too similar to the username.
    Bypass password validation and create user anyway? [y/N]: N
    Password:
    Password (again):
    Superuser created successfully.

If you press `[Enter]`, you should have successfully created a user:    

    Superuser created successfully.   

Now start the server again:

    py manage.py runserver

In the browser window, type 127.0.0.1:8000/admin/ in the address bar.

And fill in the form with the correct username and password:

`Here you can create, read, update, and delete groups and users.`