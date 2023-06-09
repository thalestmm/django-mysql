[![author](https://img.shields.io/badge/author-thalestmm-red.svg)](https://www.linkedin.com/in/thales-m-meier-44593b17b)

# **Django MySQL Template**

*All code snippets starting with `>` are commands to be executed in the terminal on the root directory.*

<details>
<summary><b><font size=4>Project Setup</font></b> </summary>

*These are basic orientations for starting a new Python project.*

Start a new virtual environment:

`> python -m venv .venv`

`> source .venv/bin/activate`

Access the project directory:

`> cd mysql`

Install dependencies:

`> pip install -r requirements.txt`

</details>

## **Database Setup**

The MySQL database is configured to be used in the `localhost` server, on port `3306`.

The selected database is called `django`, but it's meant to be used only in the development environment.

To change it, create a new `db.cnf` file on the root directory with the following options:

```
[client]
host = {database_host} // If not localhost
database = {database_name}
user = {database_user}
password = {user_password}
default-character-set = utf8
```
## **Creating a new App**

`> python3 manage.py startapp appname `

This command will create a new app directory with the chosen app name.

On `settings.py`: 
- Add the new App config to the `INSTALED_APPS` variable
  - `"appname.apps.AppnameConfig"`
    - Uppercase on app name
    - This name can be altered by changing the class name on 'appname/apps.py`
- Define models for the app on `appname/models.py`
- Register models on `appname/admin.py`
  - This enables reading models and editing them on the admin panel
- `> python3 manage.py makemigrations`
- `> python3 manage.py migrate`
- On the `mysql/urls.py` file, register the new path to the created app in the `urlpatterns` variable
  -  `path("desired_path/", include("appname.urls")),`

Now the models are created and migrated to the database.

## **Updating Views**

The url to the views was already registered in the previous step. 

When developing an API, you'll probably only need to return `httpResponse` objects in the `appname/views.py` file.

However, you can also render templates with any data you might want.

After creating a new view on `appname/views.py`, you'll need to add the desired path to run the defined function. This is done by adding the path to the `appname/urls.py` file.

## **Setting up Tests**

## **Custom Scripts**

## **Admin Panel Config**

## **Deployment**
