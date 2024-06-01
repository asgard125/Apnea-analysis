from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=64, default='', unique=True)


class Experiment(models.Model):
    name = models.CharField(max_length=64, default='', unique=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, default=None)


class UploadedFile(models.Model):
    file = models.FileField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.uploaded_on.date()


    # organizations = models.Manager()

# Create your models here.
