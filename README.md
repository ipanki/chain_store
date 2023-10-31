# Chain Store

## How to run

Start services

```
docker-compose up -d postgres redis celery celery-beat mailhog

```

Apply migrations

```
docker-compose run app pipenv run python manage.py migrate
```

Start app

```
docker-compose up app
```

## How to run locally


Activate virtual env:

```

pipenv shell

```

Install dependencies:

```

pipenv install

```

Start services:

```

docker-compose up -d postgres redis celery celery-beat mailhog

```

Run migrations

```

python manage.py migrate

```

Create super user:

```

python manage.py createsuperuser

```

Run server:

```

python manage.py runserver

```

Open Swagger:

```

http://127.0.0.1:8000/swagger/

```

