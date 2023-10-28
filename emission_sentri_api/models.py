from django.db import models


class Emissions(models.Model):
    Id = models.AutoField(primary_key=True)
    Date_Created = models.DateField()
    Accounting_Period = models.CharField(max_length=255)
    Scope1 = models.IntegerField(blank=True, null=True)
    Scope2 = models.IntegerField(blank=True, null=True)
    Scope3 = models.IntegerField(blank=True, null=True)
