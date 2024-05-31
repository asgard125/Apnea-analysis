from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=64, default='', unique=True)

    # organizations = models.Manager()

# Create your models here.
