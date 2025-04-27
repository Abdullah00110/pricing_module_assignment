from django.db import models

# Create your models here.
class PricingConfig(models.Model):
    day_of_week = models.CharField(max_length=20)
    distance_limit_km = models.FloatField()
    base_price = models.FloatField()
    additional_price_per_km = models.FloatField()
    waiting_time_free_minutes = models.IntegerField(default=3)
    waiting_charge_per_unit = models.FloatField()
    waiting_charge_unit_minutes = models.IntegerField(default=3)
    
    multiplier_upto_1hr = models.FloatField(default=1.0)
    multiplier_1_to_2hr = models.FloatField(default=1.25)
    multiplier_2_to_3hr = models.FloatField(default=2.2)
    
    is_active = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.day_of_week} Config"
    
class PricingConfigLog(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    actor = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Log: {self.config.day_of_week} - {self.action}"

