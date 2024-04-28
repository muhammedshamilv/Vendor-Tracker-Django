FROM python:3.10.6-alpine3.16

RUN apk add --no-cache git build-base linux-headers libffi-dev

# Set working directory
WORKDIR /VendorTracker

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the entire Django project
COPY . .

# Run migrations
RUN python manage.py migrate

# Set default values for environment variables if not set
ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_PASSWORD

# Create superuser
RUN python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')"

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
