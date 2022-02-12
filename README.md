# Live version
- [Home Page](https://smartedu-patika.herokuapp.com/)
 
# Prerequisites
- Python 3.9.1
- PostgreSQL 14.1
- Docker Desktop 20.10.12

# Installation

## 0. Clone the project
```bash
git clone https://github.com/oguzhancvdr/patika-django-path
```

## 1. Create a `.env` file in the project root directory.

<details>
    <summary>.env</summary>
    DEBUG=True
    SECRET_KEY=secret_key
    DATABASE_URL=psql://db_user:db_password@db:5432/db_name
    ALLOWED_HOSTS=127.0.0.1,localhost
</details>

### 1.1 in this file
- SECRET_KEY can be generated with the following command.

```python
python - c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
- DEBUG variable should be True only during project development. 

- The parameters in the DATABASE_URL variable in the .env file are the superuser username and password, the IP and port specified for the server, and the database name, respectively.

## 2. Start the project.
```bash
# create a virtual environment
python -m venv env

# activate virtual environment
env/Scripts/activate

# run docker container
cd smartedu_con
docker compose build

# apply migrations
docker exec -ti smartedu_container /bin/bash
python manage.py migrate

# start project
docker compose run app
```
[Home Page](http://127.0.0.1:8000/)
