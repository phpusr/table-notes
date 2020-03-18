import csv
from contextlib import closing

import pymysql
from django.db import IntegrityError
from django.http import HttpResponse
from pymysql.cursors import DictCursor

from app.util import parse_date
from tv_series.models import Journal, Status


def import_from_db(request):
    result = ''
    with closing(
            pymysql.connect(
                host='localhost',
                user='root',
                password='100500',
                db='Notes',
                charset='utf8',
                cursorclass=DictCursor
            )
    ) as connection:
        with connection.cursor() as cursor:
            query = 'select * from TV_series'
            cursor.execute(query)
            for row in cursor:
                journal = Journal(
                    status=Status.objects.get(pk=row['status_id']),
                    local_name=row['name'],
                    original_name=row['original_name'],
                    last_watched_season=row['last_season'],
                    last_watched_series=row['last_series'],
                    last_watched_date=row['last_date'],
                    rating=row['rating'],
                    comment=row['comment']
                )
                try:
                    journal.save()
                    result += str(journal) + '<br>'
                except IntegrityError as e:
                    if str(e).startswith('UNIQUE constraint failed:'):
                        result += str(journal) + f' ({str(e)}) <br>'
                    else:
                        raise e
    return HttpResponse(result)


def import_from_csv_file(request):
    result = ''
    with open('/home/phpusr/Downloads/Сериалы (посмотрел, смотрю) - Лист1.csv') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            print(row)
            try:
                journal = Journal.objects.get(original_name=row['Оригинальное'].strip())
            except Journal.DoesNotExist:
                journal = Journal(original_name=row['Оригинальное'].strip())
            journal.status = Status.objects.get(name=row['Статус'].strip())
            journal.local_name = row['Название'].strip()
            journal.original_name = row['Оригинальное'].strip()
            journal.last_watched_season = row['Последний просм. сезон'].strip()
            journal.last_watched_series = row['Послед. просм. серия'].strip()
            journal.last_watched_date = parse_date(row['Дата'])
            journal.rating = row['Оценка (макс. 5)'].strip()
            journal.comment = row['Комментарий'].strip()

            journal.save()
            result += str(journal) + '<br>'

    return HttpResponse(result)
