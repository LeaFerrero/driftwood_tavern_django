from django.apps import AppConfig

class AppMenuConfig(AppConfig):
    """
    Configuration for the 'app_menu' application.

    Attributes:
        default_auto_field (str): Name of the default auto-generated field for models.
        name (str): Name of the application ('app_menu').
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "app_menu"
