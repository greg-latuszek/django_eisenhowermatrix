FROM python:3.8

# where your code lives
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker workdir directory.
COPY django .
COPY requirements.txt .

# to allow building python packages that need compilation
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential
# run this command to install all dependencies
RUN pip install -r requirements.txt

# port where the Django app runs
EXPOSE 8000

# start server
#CMD ls -l \
#    && python manage.py migrate \
#    && python manage.py createsuperuser --noinput \
#    && ls -l \
#    && python manage.py runserver
CMD python manage.py runserver 0.0.0.0:8000
