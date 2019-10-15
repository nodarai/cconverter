from django.db import models


class Currency(models.Model):
    """ Model representing the currency """
    code = models.CharField(max_length=3, unique=True)
    full_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.code


class CurrencyRate(models.Model):
    """ Model representing the exchange rate for the currencies """
    convert_from = models.ForeignKey(Currency, related_name='from_currencies', on_delete=models.CASCADE)
    convert_to = models.ForeignKey(Currency, related_name='to_currencies', on_delete=models.CASCADE)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}->{}={}".format(self.convert_from.code, self.convert_to.code, self.rate)
