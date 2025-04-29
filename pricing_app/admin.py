from django.contrib import admin
from .models import PricingConfig, PricingConfigLog

@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ['day_of_week', 'is_active']
    search_fields = ['day_of_week']

@admin.register(PricingConfigLog)
class PricingConfigLogAdmin(admin.ModelAdmin):
    list_display = ['config', 'action', 'actor', 'timestamp']
    readonly_fields = ['config', 'action', 'actor', 'timestamp']
