FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE main.settings.prod

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

COPY . /app/
WORKDIR /app/
RUN ./manage.py collectstatic

EXPOSE 8000
ENTRYPOINT ./manage.py migrate && gunicorn main.wsgi:application --bind 0.0.0.0:8000 --workers 1
