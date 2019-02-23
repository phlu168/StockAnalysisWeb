from django.db import models
import datetime 

# Create your models here.

#class Stock(models.Model):
#    ticker = models.CharField(max_length=10, unique=True)
    

class StockPrice(models.Model):
    sym = models.CharField(max_length=10, default="symbol")
    date = models.DateField(default=datetime.datetime.now())
    #stock = models.ForeignKey(Stock, related_name="prices")
    open = models.DecimalField(max_digits=20, decimal_places=6, default=0)
    high = models.DecimalField(max_digits=20, decimal_places=6,  default=0)
    low = models.DecimalField(max_digits=20, decimal_places=6,  default=0)
    close = models.DecimalField(max_digits=20, decimal_places=6,  default=0)
    volume = models.DecimalField(max_digits=20, decimal_places=6,  default=0)
    def __str__(self):
        """A string representation of the model."""
        return self.sym

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True, default="symbol")
    #name = models.CharField(max_length=50, unique=True, default="name")
    startDate = models.DateField(default=datetime.datetime.now())
    endDate = models.DateField(default=datetime.datetime.now())
    def __str__(self):
        """A string representation of the model."""
        return self.symbol
    #dailyPrice = models.ForeignKey( StockPrice, on_delete=models.CASCADE, related_name="prices", default=1)