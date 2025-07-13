from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'created_at')
    list_filter = ('date', 'created_at', 'user')
    search_fields = ('title', 'description', 'user__username')
    date_hierarchy = 'created_at'
