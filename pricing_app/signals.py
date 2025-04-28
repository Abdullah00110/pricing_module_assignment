from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PricingConfig, PricingConfigLog

@receiver(post_save, sender=PricingConfig)
def create_pricing_config_log(sender, instance, created, **kwargs):
    if created:
        action = "Created"
    else:
        action = "Updated"
    PricingConfigLog.objects.create(
        config = instance,
        action = action,
        actor = "Admin"
    )