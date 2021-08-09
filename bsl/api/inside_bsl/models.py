from django.db import models


# Create your models here.
class Abonents(models.Model):
    uuid = models.UUIDField(max_length=36)
    name = models.CharField(max_length=200)
    balance = models.IntegerField()
    hold = models.IntegerField()
    status = models.BooleanField()
