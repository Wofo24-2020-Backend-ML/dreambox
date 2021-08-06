from django.db import models
from main.models import User

# Create your models here.

class CSVData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbole = models.CharField(max_length=255,null=True, blank=False )
    date = models.CharField(max_length=255,null=True, blank=False)
    open = models.CharField(max_length=255, null=True, blank=False)
    high = models.CharField(max_length=255,null=True, blank=False)
    low = models.CharField(max_length=255, null=True, blank=False)
    close = models.CharField(max_length=255, null=True, blank=False)
    volume = models.CharField(max_length=255, null=True, blank=False)
    adjclose = models.CharField(max_length=255, null=True, blank=False)




