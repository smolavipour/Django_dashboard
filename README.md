# Django_dashboard

In this project, I have a PostgreSQL (V14) database and I want to visualize it as a dashboard using Django. 
This project is done on Windows 10, and Python 3.8.8 and Django 4.0.4 are installed via Anconda.

* To set up PostgreSQL server, if the server did not start automatically, execute the command below using cmd:

<pre><code>pg_ctl.exe restart -D  "C:\Program Files\PostgreSQL\14\data"</code></pre>

## Step 1
Set up a Django project according to the guide on [Link](https://docs.djangoproject.com/en/4.0/intro/tutorial01/).
We create the project dashboard first:
<pre><code>django-admin startproject mysite</code></pre>
Inside the project, we create the main application which we call it myapp.
<pre><code>python manage.py startapp polls</code></pre>