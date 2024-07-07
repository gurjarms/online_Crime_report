from django.apps import AppConfig

class CrimeReportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Crime_Report'
    

    def ready(self):
        import Crime_Report.signals
