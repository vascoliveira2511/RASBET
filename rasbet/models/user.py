from django.db import models
from django.contrib.auth.models import AbstractUser
from .wallet import Wallet

class User(AbstractUser):
    wallet = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, verbose_name="user wallet", null=True)