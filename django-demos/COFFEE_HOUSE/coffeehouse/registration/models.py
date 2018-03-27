from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CoffeehouseUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    telepphone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        ordering=['-id']
        db_table='member'

