from django import forms
from .models import Stock_buy, Stock_sell

class Stock_buy_form(forms.ModelForm):
    class Meta:
        model=Stock_buy
        fields=('symbol','name','quantity_bought','cost','buy_date','buy_date')
        
   