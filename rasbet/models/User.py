from django.db import models

# Here we should type our models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.IntegerChoices(
        (0, 'ADMIN USER'), (1, 'SPECIAL USER'), (2, 'NORMAL USER'))
    wallet = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.email
