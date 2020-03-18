BACKUP_FILE="data/backup_db.sql"

help:
	@echo "tabular-notes Makefile"

backup-prod-db:
	@HOST="ec2-54-75-246-118.eu-west-1.compute.amazonaws.com" \
	PORT=5432 \
    DB="dd8ua7ol9r9g68" \
    USER="vvefhkdmnickmr" \
	make backup-db

restore-dev-db:
	HOST="localhost" \
	PORT=5432 \
	DB="tabular_notes" \
	USER="phpusr" \
	make restore-db

backup-db:
	@echo "=== Backuping: $(HOST)/$(DB) ==="
	@pg_dump -f $(BACKUP_FILE) -h $(HOST) -p $(PORT) -d $(DB) -U $(USER) \
		--no-password --clean --if-exists --no-owner --no-privileges

restore-db:
	@echo "=== Restoring: $(HOST)/$(DB) ==="
	@psql -h $(HOST) -p $(PORT) -U $(USER) -d $(DB) -f $(BACKUP_FILE)

