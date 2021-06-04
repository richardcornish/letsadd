from django.contrib import admin

from .models import Park


class ParkAdmin(admin.ModelAdmin):
    list_display = ('name', 'whs', 'br')


admin.site.register(Park, ParkAdmin)
