from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """
    Configuration class for the 'reviews' Django app.

    This AppConfig class provides configuration settings for the 'reviews' app,
    including specifying the default auto field and the name of the app.

    Attributes:
        default_auto_field (str): The name of the default auto field for models in this app.
            By default, it is set to 'django.db.models.BigAutoField'.
        name (str): The name of the Django app, which should match the app's directory name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
