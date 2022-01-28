# Database
1. first step is to run `python manage.py migrate`
   * it will create SQLite DB since it is default DB engine for Django 
2. next create Admin account via `python manage.py createsuperuser`
   * it will be available at `<URL>/admin/`
   * it will ask for username, email & password
3. after model change you should create migrations via `python manage.py makemigrations`
   * it will create python files under `tasks/migrations/`
   * then you perform migrations via `python manage.py migrate`
      * it changes just DB and not project files (`db.sqlite3` should not be under source control)

# Creating skeleton code
* each functional part should be treated as app -> one app == one functionality
   * `python manage.py startapp tasks` - handling tasks
   * `python manage.py startapp accounts` - handling users registration/login

# Running
* start django via `python manage.py runserver`