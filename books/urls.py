from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('csv-file-import', views.import_from_csv_file, name='csv-file-import')
]
