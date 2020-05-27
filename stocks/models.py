from django.db import models
from datetime import datetime, date
from django.utils import timezone 
# Create your models here.
class Stock_buy(models.Model):
    symbol=models.CharField(max_length=10)
    name=models.CharField(max_length=75,default='None Entered')
    quantity_bought=models.FloatField()
    cost=models.FloatField()
    buy_date=models.DateField("Buy Date(M/D/YYYY)",auto_now_add=False,auto_now=False,blank=True)
    timestamp=models.DateField(auto_now_add=True,auto_now=False,blank=True)

    def __str__(self):
        return self.symbol



class Stock_sell(models.Model):
    stock=models.ForeignKey(Stock_buy,on_delete=models.CASCADE)
    quantity_sold=models.FloatField()
    amount=models.FloatField()
    sold_date=models.DateField()

    def __str__(self):
        return f'{self.quantity_sold} at {self.amount} per share'

    