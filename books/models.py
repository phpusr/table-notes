from django.conf import settings
from django.db import models
from django.utils import timezone

from main.models import OwnerModel, NameOwnerUniqueModel, NameOwnerModel


class Author(NameOwnerUniqueModel):
    pass


class Genre(NameOwnerUniqueModel):
    pass


class Category(NameOwnerUniqueModel):
    pass


class Book(OwnerModel):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [
            ['title', 'genre']
        ]


class Source(NameOwnerModel):
    pass


class Journal(OwnerModel):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT, null=True, blank=True)

    class Status(models.IntegerChoices):
        DIDNT_READ = 1
        READING = 2
        READ = 3
        STOPPED = 4

    status = models.PositiveIntegerField(choices=Status.choices, default=Status.DIDNT_READ)

    add_date = models.DateField(default=timezone.now, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    pages_number = models.PositiveIntegerField(null=True, blank=True)

    Rating = models.IntegerChoices('Book rating', '1 2 3 4 5')
    rating = models.PositiveIntegerField(choices=Rating.choices, null=True, blank=True)

    note = models.TextField(blank=True)

    @property
    def days_spent(self):
        empty = settings.EMPTY_VALUE_DISPLAY
        if self.status == Journal.Status.DIDNT_READ or self.status == Journal.Status.STOPPED:
            return empty

        start_date = self.start_date
        end_date = self.end_date

        if self.status == Journal.Status.READING:
            end_date = timezone.now().date()

        if end_date is None or start_date is None:
            return empty

        return (end_date - start_date).days

    def __str__(self):
        return str(self.book)

    class Meta:
        unique_together = [
            ['owner', 'book']
        ]
