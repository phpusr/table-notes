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
    add_date = models.DateField(default=timezone.now, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    pages_number = models.PositiveIntegerField(null=True, blank=True)

    Rating = models.IntegerChoices('Book rating', '1 2 3 4 5')
    rating = models.PositiveIntegerField(choices=Rating.choices, null=True, blank=True)

    note = models.TextField(blank=True)

    @property
    def days_spent(self):
        if self.end_date is None or self.start_date is None:
            return '-'

        return (self.end_date - self.start_date).days

    def read(self):
        return self.end_date is not None
    read.boolean = True

    def __str__(self):
        return str(self.book)

    class Meta:
        unique_together = [
            ['owner', 'book']
        ]
