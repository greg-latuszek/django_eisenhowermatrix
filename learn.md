# Database
1. first step is to run `python manage.py migrate`
   * it will create SQLite DB since it is default DB engine for Django 
1. next create Admin account via `python manage.py createsuperuser`
   * it will be available at `<URL>/admin/`
   * it will ask for username, email & password

# Running
* start django via `python manage.py runserver`