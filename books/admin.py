from django.contrib import admin

from main.admin import OwnerAdmin, OwnerPublicAdmin
from .models import Author, Book, Source, Journal, Genre, Category

admin.site.register(Source, OwnerAdmin)

admin.site.register(Author, OwnerPublicAdmin)
admin.site.register(Genre, OwnerPublicAdmin)
admin.site.register(Category, OwnerPublicAdmin)


@admin.register(Book)
class BookAdmin(OwnerPublicAdmin):
    list_display = ['title']
    search_fields = ['title']
    autocomplete_fields = ['authors', 'genre', 'category']


@admin.register(Journal)
class JournalAdmin(OwnerAdmin):
    list_display = ['book', 'authors', 'genre', 'category', 'source', 'add_date', 'start_date', 'end_date', 'days_number',
                    'pages_number', 'note']
    autocomplete_fields = ['book', 'source']
    readonly_fields = ['authors', 'genre', 'category']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'book':
            return admin.ModelAdmin.formfield_for_foreignkey(self, db_field, request, **kwargs)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    @staticmethod
    def authors(obj):
        return ', '.join([str(a) for a in obj.book.authors.all()])

    @staticmethod
    def genre(obj):
        return obj.book.genre

    @staticmethod
    def category(obj):
        return obj.book.category
