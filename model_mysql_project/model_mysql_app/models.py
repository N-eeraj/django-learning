from django.db import models

# Create your models here.
class FormTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    mail = models.CharField(max_length=32)
    gender = models.CharField(max_length=7)
    dev = models.CharField(max_length=10)