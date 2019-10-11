from django.db import models
from django.utils import timezone

from main.models import OwnerModel, NameModel


class Author(OwnerModel, NameModel):
    pass


class Genre(OwnerModel, NameModel):
    pass


class Category(OwnerModel, NameModel):
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


class Source(OwnerModel, NameModel):
    class Meta:
        unique_together = [
            ['owner', 'name']
        ]


class Journal(OwnerModel):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT, null=True, blank=True)
    add_date = models.DateField(default=timezone.now)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    pages_number = models.PositiveIntegerField(null=True, blank=True)
    note = models.TextField(blank=True)

    @property
    def days_number(self):
        if self.end_date is None or self.start_date is None:
            return '-'

        return (self.end_date - self.start_date).days

    def __str__(self):
        return str(self.book)

    class Meta:
        unique_together = [
            ['owner', 'book']
        ]
