# Eisenhower Matrix usage

## before you start
After cloning repo please do initialize underlying database via:
* `python manage.py migrate` or 
* `python3 manage.py migrate`

Then you need to create Admin account for that DB
* do it via: `python manage.py createsuperuser`
* it will be available at `<URL>/admin/`
* it will ask for username, email & password
* don't use it for any activity inside app !!!
   * inside app create different users
  
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

### development variant 2 (using MailHog)
[Run MailHog in docker](devenv.md#mailhog).
Then your `settings.py` need:
```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = '127.0.0.1'
EMAIL_PORT = 1025
```
After clicking navbar's `Forgot Password`, providing user's email and clicking `Reset my password` you will find
reset password email displayed at http://127.0.0.1:8025/.
Go there and copy password reset link. Paste it in browser, fill new password, confirm same
and click `Change my password`.

### production variant
Comment out lines from above "development variant" and uncomment (if commented out) following inside `settings.py`:
```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_PASSWORD", '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get("ADMIN_EMAIL", '')
```
1. It requires to setup account on https://sendgrid.com/ - "email forwarder" service
2. Create there integration key: Setup Guide / Integrate / SMTP
3. Put that key in environment variable `SENDGRID_PASSWORD`
   * API keys are at `https://app.sendgrid.com/settings/api_keys`.
      * for security reasons you won't be able to see API Key there
      * you just need to create new one (for first time or if you forgot old one)
      * then write it down somewhere and put into `SENDGRID_PASSWORD` env var
4. Put your admin email inside environment variable `ADMIN_EMAIL`
   * **CAUTION**: double check which email is used for "email forwarding". It doesn't need to be same email which was used to register at SendGrid.
   * go to `https://app.sendgrid.com/settings/sender_auth`
   * find section "Single Sender verification"
   * click `Verify a Single Sender` and fill in that form:
      * those fields will map to created email fields
      * form's field `From Email Address` **MUST BE FILLED WITH ADMIN email** (created above in `before you start`) 
      * after submitting form you need to click confirmation inside email send from SendGrid into your Admin-email
   * later on you can check configured senders at `https://app.sendgrid.com/settings/sender_auth/senders`
      * look for green tick at Verified column 
6. At `Forgot Password` form fill email of app user who wants to change password
   * I'll repeat once more - it may not be admin email
   * check inbox for that email - there will be reset password email

## usage
### see all tasks
You have 3 variants of tasks list view:
* table view ![tv](django/static/img/table.svg) - shows all details in table-list form
* condensed list view ![tv](django/static/img/list-compact.svg) 
* eisenhower matrix view ![tv](django/static/img/eisenhower.svg) 

You select them via clicking proper icon in navbar.

You will always see only yours tasks.
However, if you are logged in as admin you will see all tasks - but only at table view.

### all other functionalities
Just play around - app should be intuitive :-)