from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code

class ExchangeRate(models.Model):
    currency_pair = models.CharField(max_length=7, unique=True)
    exchange_rate = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.currency_pair}: {self.exchange_rate}"