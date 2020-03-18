from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User

admin.site.site_header = f"Tabular Notes (v{settings.VERSION}-{'dev' if settings.DEBUG else 'prod'})"


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
        if len(all_friends) > 0 and current_user not in all_friends:
            all_friends.append(current_user)

        return users_to_tuple(all_friends)

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(owner__username=self.value())


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']
    readonly_fields = []
    list_filter = []

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        current_user = request.user
        if current_user.is_superuser:
            return queryset

        friends = list(current_user.friends.all())
        if current_user not in friends:
            friends.append(current_user)

        return queryset.filter(owner__in=friends)

    def get_search_results(self, request, queryset, search_term):
        is_filter_by_owner = 'owner' in request.GET

        if not (request.user.is_superuser or is_filter_by_owner):
            queryset = queryset.filter(owner__id=request.user.id)

        return super().get_search_results(request, queryset, search_term)

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'owner'):
            obj.owner = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj) and self._is_owner(request.user, obj)

    def has_delete_permission(self, request, obj=None):
        return super().has_delete_permission(request, obj) and self._is_owner(request.user, obj)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        model = db_field.related_model
        if not request.user.is_superuser and hasattr(db_field.related_model, 'owner'):
            kwargs["queryset"] = model.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_list_display(self, request):
        if request.user.is_superuser and 'owner' not in self.list_display:
            self.list_display.append('owner')

        return self.list_display

    def get_readonly_fields(self, request, obj=None):
        if 'owner' not in self.readonly_fields:
            self.readonly_fields.append('owner')

        return self.readonly_fields

    def get_list_filter(self, request, obj=None):
        if OwnerListFilter not in self.list_filter:
            self.list_filter.append(OwnerListFilter)

        return self.list_filter

    @staticmethod
    def _is_owner(user, obj):
        return obj is None or obj.owner_id == user.id or user.is_superuser


class OwnerPublicAdmin(OwnerAdmin):
    def get_queryset(self, request):
        return admin.ModelAdmin.get_queryset(self, request)

    def get_search_results(self, request, queryset, search_term):
        return admin.ModelAdmin.get_search_results(self, request, queryset, search_term)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return admin.ModelAdmin.formfield_for_foreignkey(self, db_field, request, **kwargs)

    def get_list_display(self, request):
        if 'owner' not in self.list_display:
            self.list_display.append('owner')

        return self.list_display


class JournalAdminAbstract(OwnerAdmin):
    ordering = ['-id']
    public_fields = []

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name in self.public_fields:
            return admin.ModelAdmin.formfield_for_foreignkey(self, db_field, request, **kwargs)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
