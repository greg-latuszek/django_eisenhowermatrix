# Celery

## installation
```bash
pip install -U Celery
sudo apt install rabbitmq-server
```
### install celery plugin
```bash
pip install django-celery-email
```

## start workers
Do it before sending email (before password reset)
```bash
cd django_eisenhower
celery -A tasks worker -l INFO
```
