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
    list_display = ['book', 'authors', 'genre', 'category', 'source', 'add_date', 'start_date', 'end_date', 'days_number',
                    'pages_number', 'note']
    autocomplete_fields = ['book', 'source']
    readonly_fields = ['authors', 'genre', 'category']

    @staticmethod
    def authors(obj):
        return ', '.join([str(a) for a in obj.book.authors.all()])

    @staticmethod
    def genre(obj):
        return obj.book.genre

    @staticmethod
    def category(obj):
        return obj.book.category
