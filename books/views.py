import csv
import tempfile

from django.conf import settings
from django.http import HttpResponse
from django.middleware.csrf import get_token

from app.models import User
from app.util import parse_date
from .models import Book, Author, Genre, Category, Source, Journal


def import_from_csv_file(request):
    if request.method == 'GET':
        csrf_token = get_token(request)
        result = f'''
        <h3>import_from_csv_file</h3>
        <form method='post' enctype="multipart/form-data">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}" />
            <input type="file" name="csv_file" />
            <button>Submit</button>
        </form>
        '''
        return HttpResponse(result)

    user = User.objects.get(pk=1)

    def get_or_create_object(clazz, name):
        name = name.strip()
        if name == '':
            return None

        obj, _ = clazz.objects.get_or_create(owner=user, name=name)

        return obj

    if settings.DEBUG and request.GET.get('clear') == '1':
        Journal.objects.all().delete()
        Source.objects.all().delete()
        Book.objects.all().delete()
        Category.objects.all().delete()
        Genre.objects.all().delete()
        Author.objects.all().delete()

    result = '<h3>Imported books</h3><br/>'

    upload_file = request.FILES['csv_file']
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    with tmp_file as file:
        for chunk in upload_file.chunks():
            file.write(chunk)

    with open(tmp_file.name) as file:
        reader = reversed(list(csv.DictReader(file)))

        for row in reader:
            print(row)

            book, created_book = Book.objects.get_or_create(owner=user, title=row['Название'].strip())
            if created_book:
                for author_name in row['Автор'].split(','):
                    if author_name != '':
                        book.authors.add(get_or_create_object(Author, author_name))
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
