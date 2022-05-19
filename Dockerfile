FROM python:3.8

# where your code lives
WORKDIR /code

# in preparation to install dependencies
RUN pip install --upgrade pip
# to allow building python packages that need compilation
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential
# run this command to install all dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy whole project to your docker workdir directory.
COPY django .
# port where the Django app runs
EXPOSE 8000

# start server
CMD gunicorn -b 0.0.0.0:8000 django_eisenhower.wsgi
