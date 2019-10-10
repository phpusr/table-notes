from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User

admin.site.site_header = 'Tabular Notes'


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    filter_horizontal = ('groups', 'user_permissions', 'friends')

    def get_fieldsets(self, request, obj=None):
        first_dict = self.fieldsets[0][1]
        if 'friends' not in first_dict['fields']:
            first_dict['fields'] = first_dict['fields'] + ('friends',)
        return self.fieldsets


class OwnerListFilter(admin.SimpleListFilter):
    title = 'owner list filter'
    parameter_name = 'owner'

    def lookups(self, request, model_admin):
        # TODO change it
        return [
            ['phpusr', 'phpusr'],
            ['user', 'user'],
        ]

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(owner__username=self.value())


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
    search_fields = ['name']
    readonly_fields = ['owner']
    list_filter = []

    def get_search_results(self, request, queryset, search_term):
        view_other = self.__has_view_other(request.user) and request.GET.get('owner') is not None

        if not request.user.is_superuser and not view_other:
            queryset = queryset.filter(owner__id=request.user.id)

        return super().get_search_results(request, queryset, search_term)

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'owner'):
            obj.owner = request.user
        super().save_model(request, obj, form, change)

    def has_view_permission(self, request, obj=None):
        return super().has_view_permission(request, obj) \
               and (self.__is_owner(request.user, obj) or self.__has_view_other(request.user))

    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj) and self.__is_owner(request.user, obj)

    def has_delete_permission(self, request, obj=None):
        return super().has_delete_permission(request, obj) and self.__is_owner(request.user, obj)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            kwargs["queryset"] = db_field.related_model.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_list_filter(self, request, obj=None):
        if OwnerListFilter not in self.list_filter:
            self.list_filter.append(OwnerListFilter)

        # TODO
        # if not self.__has_view_other(request.user):
        #     self.list_filter.remove(OwnerListFilter)

        return self.list_filter

    @staticmethod
    def __is_owner(user, obj):
        return obj is None or obj.owner_id == user.id or user.is_superuser

    @staticmethod
    def __has_view_other(user):
        """
        Check what user may view content of other users
        :return: If user has group with name "view_other" that return True else False
        """
        return user.is_superuser or user.groups.filter(name='view_other').count() > 0
