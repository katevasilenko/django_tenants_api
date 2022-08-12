# django_tenants_api

API of Restaurant SAAS written on Django REST Framework and django-tenants

## Installing

Python3 must be already installed

```shell
git clone https://github.com/katevasilenko/django_tenants_api
cd django_tenants_api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
set DB_HOST=<your db hostname>
set DB_NAME=<your db name>
set DB_USER=<your db username>
set DB_PASSWORD=<your db user password>
set DB_PORT=<your db port>
set SECRET_KEY=<your secret key>
python manage.py migrate
python manage.py runserver
```

Then you can run your own tenant subdomain API:

```shell
python manage.py createsuperuser
python manage.py create_tenant
python manage.py create_tenant_superuser
python manage.py runserver
```

## Features

- Powerfull admin panel
- Separate DB and domain for each restaurants
