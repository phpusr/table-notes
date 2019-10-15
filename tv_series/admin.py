from django.contrib import admin

from main.admin import OwnerAdmin, OwnerPublicAdmin, JournalAdminAbstract
from .models import Status, Journal, TVSeries

admin.site.register(Status, OwnerAdmin)


@admin.register(TVSeries)
class TVSeriesAdmin(OwnerPublicAdmin):
    list_display = ['local_name', 'original_name']
    search_fields = ['local_name', 'original_name']
    ordering = ['local_name']


class StatusListFilter(admin.SimpleListFilter):
    title = 'status list filter'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        def statuses_to_tuple(statuses):
            return [(status.pk, status.name) for status in statuses]

        current_user = request.user

        if current_user.is_superuser:
            return statuses_to_tuple(Status.objects.all())

        return statuses_to_tuple(Status.objects.filter(owner=current_user))

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(status__pk=self.value())


@admin.register(Journal)
class JournalAdmin(JournalAdminAbstract):
    list_display = ['local_name', 'original_name', 'status', 'last_watched_season', 'last_watched_series',
                    'last_watched_date', 'rating', 'comment', 'owner']
    list_filter = [StatusListFilter, 'rating']
    search_fields = ['tv_series__local_name', 'tv_series__original_name', 'comment']
    autocomplete_fields = ['tv_series', 'status']
    public_fields = ['tv_series']

    def local_name(self, obj):
        return obj.tv_series.local_name
    local_name.admin_order_field = 'tv_series__local_name'

    def original_name(self, obj):
        return obj.tv_series.original_name
    original_name.admin_order_field = 'tv_series__original_name'



