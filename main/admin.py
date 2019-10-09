from django.contrib import admin

admin.site.site_header = 'Tabular Notes'


class OwnerAdmin(admin.ModelAdmin):

    readonly_fields = ['owner']

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
