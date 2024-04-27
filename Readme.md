To install dependencies:

```
pip install -r requirements.txt
```

To apply existing migration file:

```
python manage.py migrate
```

Whenever a database migration needs to be made. Run the following commands

```
python manage.py makemigrations
```

This will generate a new migration script. Then run

```
python manage.py migrate
```

### To run the application :

make your way to the repo root

```
python manage.py runserver
```

admin site url

```
http://127.0.0.1:8000/admin/
```

To create admin user

```
python manage.py createsuperuser
```

To run test

```
pytest
```
