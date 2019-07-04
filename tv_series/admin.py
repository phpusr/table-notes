from django.contrib import admin

from tv_series.models import Status, Journal

admin.site.register(Status)


class JournalAdmin(admin.ModelAdmin):
    list_display = ['local_name', 'original_name', 'status', 'last_watched_season', 'last_watched_series',
                    'last_watched_date', 'rating', 'comment']
    exclude = ['last_watched_date']


admin.site.register(Journal, JournalAdmin)
