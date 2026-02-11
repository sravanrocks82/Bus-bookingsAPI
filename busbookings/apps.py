from django.apps import AppConfig


class BusbookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'busbookings'
    def ready(self):
        import busbookings.signals
