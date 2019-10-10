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
        def users_to_tuple(users):
            return [(user.username, user.username) for user in users]

        current_user = request.user

        if current_user.is_superuser:
            return users_to_tuple(User.objects.all())

        all_friends = list(current_user.friends.all())
        if len(all_friends) > 0:
            all_friends.append(current_user)

        return users_to_tuple(all_friends)

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(owner__username=self.value())


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
    search_fields = ['name']
    readonly_fields = ['owner']
    list_filter = []

    def get_search_results(self, request, queryset, search_term):
        owner_username = request.GET.get('owner')
        is_owner_friend = request.user.friends.filter(username=owner_username).exists()

        if not (request.user.is_superuser or is_owner_friend):
            queryset = queryset.filter(owner__id=request.user.id)

        return super().get_search_results(request, queryset, search_term)

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'owner'):
            obj.owner = request.user
        super().save_model(request, obj, form, change)

    def has_view_permission(self, request, obj=None):
        if obj is not None:
            is_owner_friend = request.user.friends.filter(pk=obj.owner_id).exists()
        else:
            is_owner_friend = False

        return super().has_view_permission(request, obj) \
               and (self._is_owner(request.user, obj) or is_owner_friend)

    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj) and self._is_owner(request.user, obj)

    def has_delete_permission(self, request, obj=None):
        return super().has_delete_permission(request, obj) and self._is_owner(request.user, obj)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            kwargs["queryset"] = db_field.related_model.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_list_filter(self, request, obj=None):
        if OwnerListFilter not in self.list_filter:
            self.list_filter.append(OwnerListFilter)

        return self.list_filter

    @staticmethod
    def _is_owner(user, obj):
        return obj is None or obj.owner_id == user.id or user.is_superuser
