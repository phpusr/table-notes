from django.db import models

from main.models import OwnerModel, NameOwnerModel


class Status(NameOwnerModel):
    pass


class TVSeries(OwnerModel):
    local_name = models.CharField(max_length=100)
    original_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.local_name} ({self.original_name})'

    class Meta:
        unique_together = [
            ['local_name', 'original_name']
        ]


class Journal(OwnerModel):
    tv_series = models.ForeignKey(TVSeries, on_delete=models.PROTECT, verbose_name='TV series')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True)
    last_watched_season = models.PositiveIntegerField(null=True, blank=True)
    last_watched_series = models.PositiveIntegerField(null=True, blank=True)
    last_watched_date = models.DateField(null=True, blank=True)

    Rating = models.IntegerChoices('TV Series rating', '1 2 3 4 5')
    rating = models.PositiveIntegerField(choices=Rating.choices, null=True, blank=True)

    comment = models.TextField(blank=True)

    def __str__(self):
        return str(self.tv_series)

    class Meta:
        unique_together = [
            ['owner', 'tv_series']
        ]

