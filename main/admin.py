from django.contrib import admin

admin.site.site_header = 'Tabular Notes'


class OwnerAdmin(admin.ModelAdmin):

    list_display = ['name', 'owner']
    list_filter = ['owner']
    search_fields = ['name']
    readonly_fields = ['owner']

    def get_queryset(self, request):
        default_queryset = super().get_queryset(request)

        if request.user.is_superuser or request.path.endswith('/change/'):
            return default_queryset

        query_owner_id = request.GET.get('owner__id__exact')
        if query_owner_id:
            return default_queryset.filter(owner__id=query_owner_id)

        return super().get_queryset(request).filter(owner__id=request.user.id)

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'owner'):
            obj.owner = request.user
        super().save_model(request, obj, form, change)

    @staticmethod
    def __check_owner(request, obj):
        return obj is None or obj.owner_id == request.user.id or request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj) and self.__check_owner(request, obj)

    def has_delete_permission(self, request, obj=None):
        return super().has_delete_permission(request, obj) and self.__check_owner(request, obj)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            kwargs["queryset"] = db_field.related_model.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
