from django.contrib import admin

from main.admin import OwnerAdmin
from tv_series.models import Status, Journal

admin.site.register(Status, OwnerAdmin)


@admin.register(Journal)
class JournalAdmin(OwnerAdmin):
    list_display = ['local_name', 'original_name', 'status', 'last_watched_season', 'last_watched_series',
                    'last_watched_date', 'rating', 'comment', 'owner']
    list_filter = ['status', 'rating']
    search_fields = ['local_name', 'original_name', 'comment']

