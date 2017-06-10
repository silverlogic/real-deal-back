# Real Deal

Real Deal is an application that allows users to see merchant offers using augmented reality on their iOS device.

## Technology

* Python 3.6
* Django 1.11
* Django Rest Framework 3.6
* SQLite database
* Digital Ocean for deployment
* CloudFlare for DNS

## Setup

Install the requirements

```
pip install -r requirements.txt
```

Make the database

```
./manage.py migrate
```

Run the development server

```
./manage.py runserver
```

You can now visit the development server at [http://localhost:8000](http://localhost:8000)
