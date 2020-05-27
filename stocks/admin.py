from django.contrib import admin
from .models import Stock_buy 

class Stock_buy_admin(admin.ModelAdmin):
    list_display=['symbol','name','quantity_bought','cost','buy_date','timestamp']
    form=Stock_buy
    list_filter=['synbol','name']
    search_fields=['symbol','name']

admin.site.register(Stock_buy)