### To install dependencies:

```
pip install -r requirements.txt
```

### To apply existing migration file:

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

### To run the application using Docker :

```
docker build --build-arg DJANGO_SUPERUSER_USERNAME=admin --build-arg DJANGO_SUPERUSER_EMAIL=admin@example.com --build-arg DJANGO_SUPERUSER_PASSWORD=adminpassword -t vendortracker .
docker run -d -p 8000:8000 --name vendortracker -t vendortracker
```

This step will also create a admin user with "admin" as username and "adminpassword" as password

We can also change the user name and password by changing values for "DJANGO_SUPERUSER_USERNAME","DJANGO_SUPERUSER_PASSWORD" from the above build command

### To stop Docker

```
docker ps
docker stop <container id>
docker rm <container id>
```

### To view API documentation

first admin should be logged in to admin portal to access swagger and redoc as security protocol
admin portal url = http://127.0.0.1:8000/admin/

To access swagger

```
http://127.0.0.1:8000/swagger/
```

#### How to use

first use token generation api which is /token POST, the body includes username and password (user accounts can be created using python manage.py createsuperuser) command since we don't have a register api. Use the generated access token to authorize the api (which is in the top right side of the swagger documentation).Use it like

```
Bearer {access token}
```

after that you can try any other APIs

Note: token expiry is about 1 hour the refresh token api is also available in the api collection

Also uploaded thunder client collection to the Repo file name=thunder-collection_VendorTracking.json you can import this collection in thunder client or you can use it as reference to try it with other platforms like Postman.

To access redoc

```
http://127.0.0.1:8000/redoc/
```
