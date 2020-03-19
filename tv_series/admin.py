from django.contrib import admin

from app.admin import OwnerPublicAdmin, JournalAdminAbstract
from .forms import JournalAdminForm
from .models import Journal, TVSeries


@admin.register(TVSeries)
class TVSeriesAdmin(OwnerPublicAdmin):
    list_display = ['local_name', 'original_name']
    search_fields = ['local_name', 'original_name']
    ordering = ['local_name']


@admin.register(Journal)
class JournalAdmin(JournalAdminAbstract):
    form = JournalAdminForm
    list_display = ['status_icon', 'rating_icon', 'local_name', 'original_name', 'status', 'last_watched_season',
                    'last_watched_episode', 'last_watched_date', 'comment', 'owner']
    list_display_links = ['local_name']
    list_filter = ['status', 'rating']
    search_fields = ['tv_series__local_name', 'tv_series__original_name', 'comment']
    autocomplete_fields = ['tv_series']
    public_fields = ['tv_series']
    ordering = ['-last_watched_date']

    def local_name(self, obj):
        return obj.tv_series.local_name
    local_name.admin_order_field = 'tv_series__local_name'

    def original_name(self, obj):
        return obj.tv_series.original_name
    original_name.admin_order_field = 'tv_series__original_name'
