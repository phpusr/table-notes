BACKUP_JSON_FILE="data/backup_db.json"
BACKUP_SQL_FILE="data/backup_db.sql"

help:
	@echo "tabular-notes Makefile"

## manage.py

dumpdata-prod:
	@DATABASE_URL=$(PROD_DB_URL) \
	make dumpdata

loaddata-prod:
	@DATABASE_URL=$(PROD_DB_URL) \
	make loaddata

dumpdata:
	@echo "=== Dumping $(PROD_DB_URL) ==="
	@pipenv run ./manage.py dumpdata --indent=2 -o $(BACKUP_JSON_FILE) #--traceback

loaddata:
	@echo "=== Restoring $(PROD_DB_URL) ==="
	@pipenv run ./manage.py flush
	@pipenv run ./manage.py loaddata $(BACKUP_JSON_FILE)

## pg_dump

backup-prod-db:
	@HOST="ec2-54-75-246-118.eu-west-1.compute.amazonaws.com" \
	PORT=5432 \
    DB="dd8ua7ol9r9g68" \
    USER="vvefhkdmnickmr" \
	make backup-db

restore-prod-db:
	@HOST="ec2-54-75-246-118.eu-west-1.compute.amazonaws.com" \
	PORT=5432 \
    DB="dd8ua7ol9r9g68" \
    USER="vvefhkdmnickmr" \
	make restore-db

backup-dev-db:
	HOST="localhost" \
	PORT=5432 \
	DB="tabular_notes" \
	USER="phpusr" \
	make backup-db

restore-dev-db:
	HOST="localhost" \
	PORT=5432 \
	DB="tabular_notes" \
	USER="phpusr" \
	make restore-db

backup-db:
	@echo "=== Dumping: $(HOST)/$(DB) ==="
	@pg_dump -f $(BACKUP_SQL_FILE) -h $(HOST) -p $(PORT) -d $(DB) -U $(USER) \
		--no-password --clean --if-exists --no-owner --no-privileges

restore-db:
	@echo "=== Restoring: $(HOST)/$(DB) ==="
	@psql -h $(HOST) -p $(PORT) -U $(USER) -d $(DB) -f $(BACKUP_SQL_FILE)

