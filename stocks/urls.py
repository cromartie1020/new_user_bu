
from django.urls import path
from . import views
urlpatterns = [
    path('stocks/',views.Stock_buy_view,name='stock' ),
    
]
