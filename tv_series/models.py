from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Journal(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    local_name = models.CharField(max_length=100, unique=True)
    original_name = models.CharField(max_length=100, unique=True)
    last_watched_season = models.IntegerField(null=True)
    last_watched_series = models.IntegerField(null=True)
    last_watched_date = models.DateField(null=True, default=timezone.now)
    rating = models.IntegerField(null=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.local_name

