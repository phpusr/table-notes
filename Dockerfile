FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE main.settings.prod

COPY ./Pipfile.lock /app/Pipfile.lock
RUN cd /app \
    && pip install --upgrade pipenv \
    && pipenv install --ignore-pipfile \
    && pipenv install gunicorn

COPY . /app/
WORKDIR /app/
RUN pipenv run ./manage.py collectstatic

EXPOSE 8000
ENTRYPOINT pipenv run ./manage.py migrate && pipenv run gunicorn main.wsgi:application --bind 0.0.0.0:8000 --workers 1
