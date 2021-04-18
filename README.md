# ArisBD
simple village community web-app

## Setup

### Dependancies

 - Python 3.6
 - Django 2.0.6


The following steps will walk you thru installation on a Mac. Linux should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.


### please follow the instructions below.


```bash
git clone https://github.com/mbrsagor/aris.git
cd aris
virtualenv venv --python=python3.6
source venv/bin/activate
pip3 install -r requirements.text
./manage.py migrate
./manage.py migrate createsuperuser
./manage.py runserver or python3 manage.py runserver

```
