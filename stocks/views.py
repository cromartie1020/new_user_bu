from django.shortcuts import render

# Create your views here.
from .forms import Stock_buy_form

def Stock_buy_view(request):
    form=Stock_buy_form(request.POST or None)
    if form.is_valid():
        form.save()
    else:    
        form=Stock_buy_form()
    return render(request,'stocks/stock_buy.html',{'form':form})  
