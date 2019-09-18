from django.db import models

# Create your models here.
class stud(models.Model):
    naam = models.CharField(max_length = 128, null = False, blank = False)
    roll = models.IntegerField(unique=True)
    sem = models.IntegerField(unique=False)

    def __str__(self):
        return str(self.roll)