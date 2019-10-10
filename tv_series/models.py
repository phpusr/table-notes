from django.db import models

from main.models import OwnerModel


class Status(OwnerModel):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Journal(OwnerModel):
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True)
    local_name = models.CharField(max_length=100)
    original_name = models.CharField(max_length=100)
    last_watched_season = models.PositiveIntegerField(null=True, blank=True)
    last_watched_series = models.PositiveIntegerField(null=True, blank=True)
    last_watched_date = models.DateField(null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.local_name

    class Meta:
        unique_together = [
            ['owner', 'local_name'],
            ['owner', 'original_name']
        ]

