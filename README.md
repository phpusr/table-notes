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

<img src="https://i.imgur.com/9G6VE61.png" width="1000px"></br>

__View and edit entry of journal__

<img src="https://i.imgur.com/NGOCZHG.png" width="500px">

#### Data fields

- Local name series
- Original name series
- Watch status (watching, full watched, waiting next season etc.)
- Last watched season
- Last watched episode
- Last watched date
- Your rating
- Comment

### books

Module for saving information about read books

__Viewed read books journal__

<img src="https://i.imgur.com/Rs8tTja.png" width="1000px"></br>

__View and edit entry of journal__

<img src="https://i.imgur.com/Zdm2kZy.png" width="500px">

#### Data fields

- Title
- Authors
- Genre
- Category
- Source (How did you find out?)
- Status (reading, done, stopped etc.)
- Add date
- Start reading date
- End reading date
- Days spent
- Pages number
- Note


How to run
----------

### Development mode

Install [Python 3](https://www.python.org/)

Install [PosgreSQL](https://www.postgresql.org/)

Install dependencies

```bash
pip install --upgrade pipenv
pipenv install --dev
```

Create DB (once)

```bash
createdb -U postgres -O <username> tabular_notes
pipenv run ./manage.py migrate
```

Run

```bash
pipenv run ./manage.py runserver [port]
```

### Production mode

Install [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/)
 
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

**v1.5 (19.03.2020)**

- Added book rating
- Added book reading status
- Added status icons
- Added rating icons
- Updated Django to 3.0.4 and dependencies

**v1.4 (15.10.2019)**

- Removed `backup_prod_db.py` (moved to my scripts)
- Moved TV series to separate table
- Added sort ordering for all objects
- Added sorting by name fields for journals
- Changed prod DB version

**v1.3 (14.10.2019)**

- Changed DB to PostgresQL
- Fixed ReadBookFilter
- Added ability to hide filter
- Changed width of columns for books journal

**v1.2 (12.10.2019)**

- Added "books" module

**v1.1 (10.10.2019)**

- Added multi user ability

**v1.0 (07.07.2019)**

- Added "tv_series" module
 