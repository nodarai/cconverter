# Currency Converter with Django

## Running the project

Clone the project
```bash
git clone https://github.com/nodarai/cconverter
```

Create `.env` file with the necessary variables

Create and setup a virtualenv
```bash
virtualenv -p python3.6 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the migrations to create a database and tables
```bash
python manage.py migrate
```

Load the initial data
```bash
python manage.py loaddata convert/fixtures/currencies.json
```

Run the celery beat
```bash
celery -A cconverter beat -l debug
```

Run a celery worker
```bash
celery -A cconverter worker -l debug
```

Run the project in development mode
```bash
python manage.py runserver
```

Optionnally, create a superuser to access the admin interface
```bash
python manage.py createsuperuser
```
And follow the instructions.  
Django Admin interface will be available at [http://localhost:8000/admin/](http://localhost:8000/admin/)

:warning: The documentation, alongside with interactive API will be available at [http://localhost:8000/docs/](http://localhost:8000/docs/)
