# Getting Started

## First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/sunithvs/TravelBuddy-backend.get
    $ cd TravelBuddy-backend

## Activate the virtualenv for your project:

    for windows
    $ python -m venv venv 
    $ venv\Scripts\activate
    
    for ubuntu
    $ python3 -m venv venv 
    $ source venv\bin\activate

## Install project dependencies:

    $ pip install -r requirements.txt

## Then simply apply the migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate

## You can now run the development server:

    $ python manage.py runserver

## Create a superuser account:

    $ python manage.py createsuperuser

### You can now login to the admin site at http://127.0.0.1:8000/admin/ using the superuser account you just created

### Add necessary data and create permissions for useragent group
