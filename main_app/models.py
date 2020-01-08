from django.db import models
from django.urls import reverse

# Create your models here.

SHIFTSEGS = (
    ('1','1st shift'),
    ('2','2nd shift'),
    ('3','3rd shift')
)
AMMOT = (
    ('T','Tracer Rounds'),
    ('HS','Hog Scatter Shot'),
    ('BP','Bristle Piercing Rounds')
)

class Slingshot(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    ammo = models.CharField(
        max_length=1,
        choices=AMMOT,
        default=AMMOT[0][0]
    )

class Chimp(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    slingshots = models.ManyToManyField(Slingshot)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'chimp_id': self.id})

class Shift(models.Model):
    date = models.DateField('shift date')
    shiftSeg = models.CharField(
        max_length=1,
        choices=SHIFTSEGS,
        default=SHIFTSEGS[0][0]
        )

    chimp = models.ForeignKey(Chimp, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_shiftSeg_display()} on {self.date}"