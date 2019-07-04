from django.urls import path

from . import views

app_name = 'tv_series'
urlpatterns = [
    path('db-import', views.import_from_db, name='import_from_db')
]
