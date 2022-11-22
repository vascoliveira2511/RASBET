from django.db import models

class Market(models.Model):
    key = models.CharField(max_length=100, unique=True)  # key of the market

    def __str__(self):
        return self.key
