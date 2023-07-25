from django.contrib import admin
from django.contrib.admin.models import LogEntry


class LogAdmin(admin.ModelAdmin):
    model = LogEntry
    list_filter = ('user', 'content_type', 'object_repr')

admin.site.register(LogEntry, LogAdmin)
