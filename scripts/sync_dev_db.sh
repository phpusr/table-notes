#!/bin/sh

BACKUP_FILE=$PWD/../data/backup_db.json

echo "Dump creating"
export DJANGO_SETTINGS_MODULE=main.settings.backup
cd ..
pipenv run ./manage.py dumpdata --indent=2 -o "$BACKUP_FILE"

echo "Cleaning data"
export DJANGO_SETTINGS_MODULE=main.settings.dev
pipenv run ./manage.py flush

echo "Dump importing"
pipenv run ./manage.py loaddata "$BACKUP_FILE" -e contenttypes.contenttype -e auth.permission
