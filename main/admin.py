from django.contrib import admin

admin.site.site_header = 'Tabular Notes'


class OwnerAdmin(admin.ModelAdmin):

    list_display = ['name', 'owner']
    list_filter = ['owner']
    search_fields = ['name']
    readonly_fields = ['owner']

    def get_queryset(self, request):
        default_queryset = super().get_queryset(request)
        has_view_other = self.__has_view_other(request.user)

        if request.user.is_superuser or (has_view_other and request.path.endswith('/change/')):
            return default_queryset

        query_owner_id = has_view_other and request.GET.get('owner__id__exact')
        if query_owner_id:
            return default_queryset.filter(owner__id=query_owner_id)

        return super().get_queryset(request).filter(owner__id=request.user.id)

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'owner'):
            obj.owner = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj) and self.__is_owner(request, obj)

    def has_delete_permission(self, request, obj=None):
        return super().has_delete_permission(request, obj) and self.__is_owner(request, obj)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            kwargs["queryset"] = db_field.related_model.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    @staticmethod
    def __is_owner(request, obj):
        return obj is None or obj.owner_id == request.user.id or request.user.is_superuser

    @staticmethod
    def __has_view_other(user):
        """
        Check what user may view content of other users
        :return: If user has group with name "view_other" that return True else False
        """
        return user.groups.filter(name='view_other').count() > 0
