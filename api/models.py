from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=64, default='', unique=True)
    age = models.FloatField(null=True, blank=True, default=0.0)
    sex = models.FloatField(null=True, blank=True, default=0.0)
    height = models.FloatField(null=True, blank=True, default=0.0)
    weight = models.FloatField(null=True, blank=True, default=0.0)
    pulse = models.FloatField(null=True, blank=True, default=0.0) 
    BPsys = models.FloatField(null=True, blank=True, default=0.0)
    BPdia = models.FloatField(null=True, blank=True, default=0.0)
    ODI = models.FloatField(null=True, blank=True, default=0.0)


class Experiment(models.Model):
    name = models.CharField(max_length=64, default='', unique=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, default=None)


class UploadedFile(models.Model):
    file = models.FileField()
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uploaded_on.date()

