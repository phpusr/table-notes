from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from main.admin import OwnerAdmin, OwnerPublicAdmin, JournalAdminAbstract
from .models import Author, Book, Source, Journal, Genre, Category


@admin.register(Source)
class SourceAdmin(OwnerAdmin):
    list_display = ['name', 'journals']
    readonly_fields = ['journals']

    @staticmethod
    def journals(obj):
        def journal_to_link(journal):
            return f'<a href="{reverse("admin:books_journal_change", args=[journal.pk])}">{str(journal)}</a>'

        return format_html('<br/>'.join([journal_to_link(x) for x in obj.journal_set.all()]))


admin.site.register(Author, OwnerPublicAdmin)
admin.site.register(Genre, OwnerPublicAdmin)
admin.site.register(Category, OwnerPublicAdmin)


@admin.register(Book)
class BookAdmin(OwnerPublicAdmin):
    list_display = ['title']
    search_fields = ['title']
    ordering = ['title']
    autocomplete_fields = ['authors', 'genre', 'category']


class ReadBookFilter(admin.SimpleListFilter):
    title = 'read book'
    parameter_name = 'read'

    def lookups(self, request, model_admin):
        return ('yes', 'Yes'), ('no', 'No')

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(end_date__isnull=False)
        elif self.value() == 'no':
            return queryset.filter(end_date__isnull=True)


@admin.register(Journal)
class JournalAdmin(JournalAdminAbstract):
    list_display = ['book_title', 'read', 'authors', 'genre', 'category', 'source', 'add_date', 'start_date', 'end_date',
                    'days_spent', 'pages_number', 'note']
    autocomplete_fields = ['book', 'source']
    readonly_fields = ['read', 'authors', 'genre', 'category', 'days_spent']
    list_filter = [ReadBookFilter, 'book__category', 'book__genre']
    search_fields = ['book__title', 'book__authors__name', 'book__genre__name', 'book__category__name', 'source__name',
                     'note']
    date_hierarchy = 'end_date'
    public_fields = ['book']

    def book_title(self, obj):
        return obj.book.title

    book_title.admin_order_field = 'book__title'

    @staticmethod
    def authors(obj):
        return ', '.join([str(a) for a in obj.book.authors.all()])

    @staticmethod
    def genre(obj):
        return obj.book.genre

    @staticmethod
    def category(obj):
        return obj.book.category

    class Media:
        js = ['admin/js/list_filter_collapse.js']
        css = {'all': ['admin/css/books/journal.css']}
