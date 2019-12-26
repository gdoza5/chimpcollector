from django.db import models

# Create your models here.

class Chimp(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    description = models.TextField(max_length=250)
    age = models.IntegerField()