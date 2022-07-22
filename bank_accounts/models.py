from django.db import models

# Create your models here.
from bank_auth.models import BankUser


class BankAccount(models.Model):
    user = models.OneToOneField(BankUser, on_delete=models.CASCADE, primary_key=True)
    type = models.CharField(max_length=30)
    date_created = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
