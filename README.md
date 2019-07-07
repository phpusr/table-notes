Tabular Notes
=============

Simple application written in Django for keeping tabular notes.

The application consists of several modules: tv_series, ...

In each module you can add, edit, delete, sort and filter records.

Modules
-------

### tv_series

Module for saving information about watched TV series.

__Viewed TV series journal__

<img src="https://i.imgur.com/Rg7yG5r.png" width="1000px" /></br>

__View and edit record of journal__

<img src="https://i.imgur.com/RY1jfT6.png" width="500px" />

#### Data fields

- Local name series
- Original name series
- Watch status (watching, full watched, waiting next season etc.)
- Last watched season
- Last watched series
- Last watched date
- Your rating
- Comment

How to run
----------

### Develop mode

- Install Python 3
- `pip install --upgrade pip && pip install -r requirements.txt`
- Create db: `./manage.py migrate`
- `./manage.py runserver [port]`

### Production mode

- Install [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/)
- Create production db (once): `export DJANGO_SETTINGS_MODULE=main.settings_prod && ./manage.py migrate` 
- Run docker container (it will build container if not exists): `docker-compose up` 
    - Force rebuild docker container and run: `docker-compose up --build`
- Open in browser: `http://localhost:8001`
 