from django.apps import AppConfig


class ServidoresAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'servidores_app'

class SeuAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'seu_app'

    def ready(self):
        import seu_app.signals
