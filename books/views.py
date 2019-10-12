import csv
from django.http import HttpResponse

from main.models import User
from .models import Book, Author, Genre, Category, Source, Journal


def import_from_csv_file(request):
    result = ''

    with open('/home/phpusr/Downloads/Книги - Ответы на форму (1).csv') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            print(row)

            user = User.objects.get(pk=1)

            book, created_book = Book.objects.get_or_create(owner=user, title=row['Название'].strip())
            if created_book:
                author, _ = Author.objects.get_or_create(owner=user, name=row['Автор'].strip())
                genre, _ = Genre.objects.get_or_create(owner=user, name=row['Жанр'].strip())
                category, _ = Category.objects.get_or_create(owner=user, name=row['Категория'].strip())

                book.authors.add(author)
                book.genre = genre
                book.category = category
                book.save()

            source, _ = Source.objects.get_or_create(owner=user, name=row['Источник'].strip())
            journal, created_journal = Journal.objects.get_or_create(owner=user, book=book, source=source)

            if created_journal:
                result += str(journal)

    return HttpResponse(result)
