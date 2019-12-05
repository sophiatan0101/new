from django.db import models

# Create your models here.
# Create your models here.

class squirrel(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    uniqueid = models.CharField(max_length=150)
    shift = models.CharField(max_length=150)
    Date = models.IntegerField()
    Age = models.CharField(max_length=150)
    furcolor = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    specificlocation = models.CharField(max_length=150)
    running = models.CharField(max_length=150)
    chasing = models.CharField(max_length=150)
    climbing = models.CharField(max_length=150)
    eating = models.CharField(max_length=150)
    foraging = models.CharField(max_length=150)
    otheractivities = models.CharField(max_length=150)
    kuks = models.CharField(max_length=150)
    quaas = models.CharField(max_length=150)
    moans = models.CharField(max_length=150)
    tailflags = models.CharField(max_length=150)
    tailtwitches = models.CharField(max_length=150)
    approaches = models.CharField(max_length=150)
    indifferent = models.CharField(max_length=150)
    runsfrom = models.CharField(max_length=150)
    def __str__(self):
        return self.name
