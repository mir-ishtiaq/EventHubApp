from django.contrib import admin
from .models import Category, Location, Event

admin.site.register(Category)
admin.site.register(Location)


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'user']
    # other customization

admin.site.register(Event, EventAdmin)
