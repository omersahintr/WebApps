from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"temp_app/first.html")

def currency(request):
    currency_dict = {"Dollar":38.8, "Euro":44.05, "Gold":3982.44, "BTC":4237678.26}

    return render(request,"temp_app/currency.html",context=currency_dict)
