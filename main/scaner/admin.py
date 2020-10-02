from django.contrib import admin
from scaner.models import Scan


@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at')
    list_filter = ('code',)
    search_fields = ('code',)
    #prepopulated_fields = {'slug': ('code', 'pk')}
    ordering = ('-created_at',)
