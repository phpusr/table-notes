from django.contrib import admin

from main.admin import OwnerAdmin, OwnerPublicAdmin
from .models import Author, Book, Source, Journal, Genre, Category


@admin.register(Source)
class SourceAdmin(OwnerAdmin):
    list_display = ['name', 'journals']
    readonly_fields = ['journals']

    @staticmethod
    def journals(obj):
        return ', '.join([str(x) for x in obj.journal_set.all()])


admin.site.register(Author, OwnerPublicAdmin)
admin.site.register(Genre, OwnerPublicAdmin)
admin.site.register(Category, OwnerPublicAdmin)


@admin.register(Book)
class BookAdmin(OwnerPublicAdmin):
    list_display = ['title']
    search_fields = ['title']
    autocomplete_fields = ['authors', 'genre', 'category']


class ReadBookFilter(admin.SimpleListFilter):
    title = 'read book'
    parameter_name = 'read'

    def lookups(self, request, model_admin):
        return ('yes', 'Yes'), ('no', 'No')

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(end_date__isnull=True)
        elif self.value() == 'now':
            return queryset.filter(end_date__isnull=False)


@admin.register(Journal)
class JournalAdmin(OwnerAdmin):
    list_display = ['book', 'read', 'authors', 'genre', 'category', 'source', 'add_date', 'start_date', 'end_date',
                    'days_number', 'pages_number', 'note']
    autocomplete_fields = ['book', 'source']
    readonly_fields = ['authors', 'genre', 'category']
    list_filter = [ReadBookFilter, 'book__category', 'book__genre']
    search_fields = ['book__title', 'book__authors__name', 'book__genre__name', 'book__category__name', 'source__name',
                     'note']

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
