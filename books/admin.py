from django.contrib import admin

from main.admin import OwnerAdmin
from .models import Author, Book, Source, Journal

admin.site.register(Author, admin.ModelAdmin)
admin.site.register(Book, admin.ModelAdmin)
admin.site.register(Source, admin.ModelAdmin)


@admin.register(Journal)
class JournalAdmin(OwnerAdmin):
    list_display = ['book', 'add_date']
