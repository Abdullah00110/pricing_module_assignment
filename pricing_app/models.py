from django.db import models

class PricingConfig(models.Model):
    day_of_week = models.CharField(max_length=10)
    distance_limit_km = models.FloatField()
    base_price = models.FloatField()
    additional_price_per_km = models.FloatField()

    waiting_time_free_minutes = models.IntegerField()
    waiting_charge_per_unit = models.FloatField()
    waiting_charge_unit_minutes = models.IntegerField()

    time_multipliers = models.JSONField(default=dict)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.day_of_week} Config"

class PricingConfigLog(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # Created / Updated
    actor = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} by {self.actor} on {self.timestamp}"
