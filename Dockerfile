FROM python:3.9.1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install pipenv
COPY Pipfile /app/
RUN pipenv install --deploy
COPY . /app/