from django.apps import AppConfig

class Jj2appConfig(AppConfig):
    name = 'coffeehouse.jj2app'
    def ready(self):
        import coffeehouse.jj2app.signals

