# **Django MySQL Template**

*All code snippets starting with `>` are commands to be executed in the terminal on the root directory.*

## **Database Setup**
---

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
---

`> python3 manage.py startapp appname `

This command will create a new app directory with the chosen app name.

On `settings.py`: 
- Add new App config to INSTALED_APPS
  - `"appname.apps.AppnameConfig"`
  - Uppercase on app name
- Define models for the app on `appname/models.py`
- Register models on `appname/admin.py`
  - This enables reading models and editing them on the admin panel
- `> python3 manage.py makemigrations`
- `> python3 manage.py migrate`

Now the models are created and migrated to the database.
