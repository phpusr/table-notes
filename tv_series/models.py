from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Journal(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    local_name = models.CharField(max_length=100)
    original_name = models.CharField(max_length=100)
    last_watched_season = models.IntegerField()
    last_watched_series = models.IntegerField()
    last_watched_date = models.DateField(default=timezone.now)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.local_name

