from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', "password", "date_joined")
    search_fields = ('email', 'username')
    readonly_fields = ("id", "date_joined")


admin.site.register(User, UserAdmin)
