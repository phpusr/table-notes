import pymysql
from contextlib import closing
from django.db import IntegrityError
from django.http import HttpResponse
from pymysql.cursors import DictCursor

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
