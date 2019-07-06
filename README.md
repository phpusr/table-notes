Tabular Notes
=============

Simple application written in Django for keeping tabular notes.

The application consists of several modules: tv_series, ...

In each module you can add, edit, delete, sort and filter records.

Modules
-------

### tv_series

Module for saving information about watched TV series.

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
- `./manage.py runserver [port]`

### Production mode

- Install Docker and Docker Compose
- Run docker container (it will build container if not exists): `docker-compose up` 
- Force rebuild docker container and run: `docker-compose up --build`
 