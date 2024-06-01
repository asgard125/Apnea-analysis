from django.contrib import admin

from .models import Patient, Experiment


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    pass

# Register your models here.
