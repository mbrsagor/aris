# ArisBD
simple village community web-app

## Setup

### Dependancies
 -Python 3.6 / Django 2.0.6

The following steps will walk you thru installation on a Mac. Linux should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.

### Installing Geospatial libraries

Create vritualenv
```
virtualenv venv --python=python3.6
```

Then active the virtualenv
```
source venv/bin/activate
```

Install Django
```
pip3 install django
```

```
pip3 install -r requirements.text
```

Last run two command
```
./manage.py migrate
./manage.py runserver or python3 manage.py runserver
```
