from django.db import models

# Create your models here.
class datachange(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)
    location = models.CharField
