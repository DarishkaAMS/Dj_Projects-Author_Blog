from django.contrib import admin
from authentication.models import USER

# Register your models here.


class USERAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "password")
    #pass

admin.site.register(USER, USERAdmin)
