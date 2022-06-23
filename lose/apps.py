from django.apps import AppConfig


class LoseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lose'
    
    def ready(self): #new
        import lose.signals #new
