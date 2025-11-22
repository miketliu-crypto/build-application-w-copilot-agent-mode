from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'duration_minutes', 'calories', 'performed_at')
    list_filter = ('performed_at', 'user')
    search_fields = ('name',)
