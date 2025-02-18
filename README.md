# django-educa
An online learning platform using Django

## Requirement

Before you begin, make sure you have the following installed:
- Python 3.11 or higher
- pip (Python package installer)
- venv (Python virtual environment manager)
- git (version control system)
- docker (containerization platform)

We will use Django version >=5.1.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/eltinawh/django-myshop.git

# navigate to the project directory
cd django-myshop
```

### 2. Set up a virtual environment
```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment (Linux/MacOS)
source .venv/bin/activate
```

### 3. Install Memcached or Redis docker image
With rarely changing contents and potentially increasing traffic, we will apply caching to queries, calculation results, or rendered content to avoid expensive operations in the subsequent requests that need to return same data. You can choose to use Memcached or Redis. Pull the docker image and run the docker container with these commands.

Memcached
```bash
docker pull memcached:1.6.36

docker run -it --rm --name memcached -p 11211:11211 memcached:1.6.36 -m 64
```
Make sure the setting for CACHES in the `educa/settings.py` file is as follows
```
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
    }
}
```


Redis
```bash
docker pull redis:7:4:2

docker run -it --rm --name redis -p 6379:6379 redis:7:4:2
```
Make sure the setting for CACHES in the `educa/settings.py` file is as follows
```
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply migrations

Run the following commands to create the necessary database tables 
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

To access the Django admin panel, create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up the admin credentials.

### 7. Load course subject data

Some of the course subjects are already populated in a fixture file (`courses/fixtures/ubjects.json`). Run this command to load that data to the database.
```bash
python manage.py loaddata subjects.json
```

### 8. Run the development server

Start the development server to verify everything is working correctly.
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to see the application.


## Documentation

[Official Django Documentation](https://www.djangoproject.com/)