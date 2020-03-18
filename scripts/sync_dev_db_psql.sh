#!/bin/sh

BACKUP_FILE=$PWD/../data/backup_db.sql

echo ">> Dumping"
HOST="172.23.0.3"
DB="tabular_notes"
USER="tabular_notes"
pg_dump -f "$BACKUP_FILE" -h $HOST -d $DB -U $USER --no-password --clean --if-exists --no-owner --no-privileges

echo ">> Restoring"
HOST="ec2-54-75-246-118.eu-west-1.compute.amazonaws.com"
DB="tabular_notes"
USER="tabular_notes"
psql -h $HOST -U $USER -d $DB -f "$BACKUP_FILE"
