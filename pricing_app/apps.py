from django.apps import AppConfig

class PricingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pricing_app'

    def ready(self):
        import pricing_app.signals
