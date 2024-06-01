from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=64, default='', unique=True)


class Experiment(models.Model):
    name = models.CharField(max_length=64, default='', unique=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, default=None)

    # organizations = models.Manager()

# Create your models here.
