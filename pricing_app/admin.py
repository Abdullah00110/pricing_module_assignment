from django.contrib import admin
from .models import PricingConfig, PricingConfigLog
from .forms import PricingConfigForm

@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    form = PricingConfigForm 
    list_display = ('day_of_week', 'base_price', 'distance_limit_km', 'is_active')
    list_filter = ('day_of_week', 'is_active')
    search_fields = ('day_of_week',)

@admin.register(PricingConfigLog)
class PricingConfigLogAdmin(admin.ModelAdmin):
    list_display = ('config', 'action', 'actor', 'timestamp')
    list_filter = ('action',)
    search_fields = ('actor',)
