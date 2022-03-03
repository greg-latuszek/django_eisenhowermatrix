# Eisenhower Matrix usage

## before you start
After cloning repo please do initialize underlying database via:
* `python manage.py migrate` or 
* `python3 manage.py migrate`

## starting
* `python manage.py runserver` or 
* `python3 manage.py runserver`

## registration
Before you can use app you need to register - click `Register` at right side of navigation bar (shortly **navbar**),
fill form and click `Sign Up`.

## login
Registration won't let you in. You must `Log In` using just registered credentials.
After successful login you may use app - create new tasks and mark them
according to rules of [Eisenhower Matrix](https://www.eisenhower.me/eisenhower-matrix/).

## password reset
Whenever you want to restore forgotten password please click `Forgot Password` in navbar.
Then provide email of user that was registered previously in app via navbar's `Register` link.
If given email is wrong (was not registered or you've made typo) no action will happen - that is
for security reasons.

### development variant
Uncomment (if commented out) following lines inside `settings.py`:
```python
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))
```
After clicking navbar's `Forgot Password`, providing user's email and clicking `Reset my password` you will find
reset password email dumped inside folder `sent_emails`.
Go there and copy password reset link. Paste it in browser, fill new password, confirm same
and click `Change my password`.

## usage
### see all tasks
You have 3 variants of tasks list view:
* table view ![tv](static/img/table.svg) - shows all details in table-list form
* condensed list view ![tv](static/img/list-compact.svg) 
* eisenhower matrix view ![tv](static/img/eisenhower.svg) 

You select them via clicking proper icon in navbar.

### all other functionalities
Just play around - app should be intuitive :-)