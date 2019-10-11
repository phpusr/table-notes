from django.db import models
from django.utils import timezone

from main.models import OwnerModel


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Source(OwnerModel):
    name = models.CharField(max_length=100)


class Journal(OwnerModel):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    add_date = models.DateField(default=timezone.now)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    pages_number = models.PositiveIntegerField(null=True, blank=True)
    note = models.TextField(blank=True)

    @property
    def days_count(self):
        return (self.end_date - self.start_date).days

    def __str__(self):
        return '-'
