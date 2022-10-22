import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app-tasks')
app.config_from_object('django.conf:settings', namespace='CELERY')
# It is here because setting it through settings.py doesn't work
app.conf.update(beat_schedule_filename=f'{settings.BASE_DIR}/data/celerybeat-schedule/data.db')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'backup-db-task': {
        'task': 'backup.tasks.backup_db_task',
        'schedule': crontab(hour=0, minute=0)
    }
}
