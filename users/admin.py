from django.contrib import admin
from . import models


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'role')
    search_fields = ('id', 'username')
    list_filter = ('role',)


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

admin.site.register(models.User, UsersAdmin)
admin.site.register(models.Profile, ProfilesAdmin)