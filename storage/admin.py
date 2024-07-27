from django.contrib import admin
from .models import StorageItem

@admin.register(StorageItem)
class StorageItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'created_at', 'updated_at')
    search_fields = ('name',)