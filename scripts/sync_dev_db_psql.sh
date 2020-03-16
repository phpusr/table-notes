#!/bin/sh

BACKUP_FILE=$PWD/../data/backup_db.sql

echo ">> Dumping"
pg_dump -f "$BACKUP_FILE" -h 172.23.0.3 -d tabular_notes -U tabular_notes --create --clean --if-exists --no-owner --no-privileges

echo ">> Restoring"
psql -d tabular_notes -f "$BACKUP_FILE"
