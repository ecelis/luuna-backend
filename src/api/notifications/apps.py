from django.apps import AppConfig
from django.db.models.signals import post_save


class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "notifications"

    def ready(self):
        from .signals.update_product import save_product

        post_save.connect(save_product)
