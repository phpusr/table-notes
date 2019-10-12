Tabular Notes
=============

Simple multi user application written in Django for keeping tabular notes.

The application consists of several modules: tv_series, books.

In each module you can add, edit, delete, sort and filter records.

Modules
-------

### tv_series

Module for saving information about watched TV series

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

### books

Module for saving information about read books

__Viewed read books journal__

<img src="https://i.imgur.com/cfNVvY4.png" width="1000px" /></br>

__View and edit record of journal__

<img src="https://i.imgur.com/xXAzw8M.png" width="500px" />

#### Data fields

- Title
- Authors
- Genre
- Category
- Source (How did you find out?)
- Add date
- Start reading date
- End reading date
- Days spent
- Pages number
- Note


How to run
----------

### Developed mode

Install Python 3

Install dependencies

```bash
pip install --upgrade pip && pip install -r requirements.txt
```

Create DB (once)

`./manage.py migrate`

Run

```bash
./manage.py runserver [port]
```

### Production mode

Install [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/)

Create production DB (once)

```bash
export DJANGO_SETTINGS_MODULE=main.settings_prod && ./manage.py migrate
```
 
Run docker container (it will build container if not exists)

```bash
docker-compose up
```

Or force rebuild docker container and run

```bash
docker-compose up --build
```

Open in browser `http://localhost:8001`

Changelist
----------

- v1.0 (07.07.2019)
    - Add "tv_series" module
- v1.1 (10.10.2019)
    - Add multi user ability
- v1.2 (12.10.2019)
    - Add "books" module
