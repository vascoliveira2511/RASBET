from django.db import models

class Wallet(models.Model):
    balance = models.FloatField(default=0.0)
    iban = models.CharField(max_length=100, null=True)