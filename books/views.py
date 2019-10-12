import csv
from django.http import HttpResponse

from main.models import User
from main.util import parse_date
from .models import Book, Author, Genre, Category, Source, Journal


def import_from_csv_file(request):
    user = User.objects.get(pk=1)

    def get_or_create_object(clazz, name):
        name = name.strip()
        if name == '':
            return None

        obj, _ = clazz.objects.get_or_create(owner=user, name=name)

        return obj

    if request.GET.get('clear') == '1':
        Journal.objects.all().delete()
        Source.objects.all().delete()
        Book.objects.all().delete()
        Category.objects.all().delete()
        Genre.objects.all().delete()
        Author.objects.all().delete()

    result = ''

    with open('/home/phpusr/Downloads/Книги - Ответы на форму (1).csv') as csv_file:
        reader = reversed(list(csv.DictReader(csv_file)))

        for row in reader:
            print(row)

            book, created_book = Book.objects.get_or_create(owner=user, title=row['Название'].strip())
            if created_book:
                author = get_or_create_object(Author, row['Автор'])
                if author is not None:
                    book.authors.add(author)
                book.genre = get_or_create_object(Genre, row['Жанр'])
                book.category = get_or_create_object(Category, row['Категория'])
                book.save()

            source = get_or_create_object(Source, row['Источник'])
            pages_number = row['Кол-во страниц'].replace('~', '')
            pages_number = int(pages_number) if pages_number != '' else None
            journal, created_journal = Journal.objects.get_or_create(
                owner=user, book=book, source=source,
                add_date=parse_date(row['Дата добавления']),
                start_date=parse_date(row['Дата начала']),
                end_date=parse_date(row['Дата выполнения']),
                pages_number=pages_number,
                note=row['Заметки']
            )

            if created_journal:
                result += str(journal) + '<br>'

    return HttpResponse(result)
