from django.contrib import admin

from main.admin import OwnerAdmin
from .models import Author, Book, Source, Journal, Genre, Category

admin.site.register(Source, OwnerAdmin)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    autocomplete_fields = ['authors', 'genre', 'category']


@admin.register(Journal)
class JournalAdmin(OwnerAdmin):
    list_display = ['book', 'source', 'add_date', 'start_date', 'end_date', 'days_number', 'pages_number', 'note']
    autocomplete_fields = ['book', 'source']
