FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV DEBUG False

WORKDIR /app/

COPY Pipfile /app/Pipfile
RUN pip install --upgrade pipenv && pipenv install

COPY . /app/
RUN pipenv run ./manage.py collectstatic

EXPOSE 8000
ENTRYPOINT pipenv run ./manage.py migrate \
            && pipenv run gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 1
