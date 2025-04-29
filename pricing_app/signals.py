from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PricingConfig, PricingConfigLog

@receiver(post_save, sender=PricingConfig)
def log_pricing_config_changes(sender, instance, created, **kwargs):
    action = "Created" if created else "Updated"
    PricingConfigLog.objects.create(
        config=instance,
        action=action,
        actor="Admin"
    )
