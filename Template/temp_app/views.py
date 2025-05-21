from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"temp_app/first.html")

def currency(request):
    currency_dict = {"Dollar":[37.7,38.8], 
                     "Euro":[43.55,44.05], 
                     "Gold":[3890.05,3982.44], 
                     "BTC":{"Ethereum":100590.84,"Doge":9.15,"Lite":3794.85}}

    return render(request,"temp_app/currency.html",context=currency_dict)
