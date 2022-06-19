from django.contrib import admin
from cash.models import Cash


@admin.register(Cash)
class CashAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'total_cash', 
        'action', 
    ]