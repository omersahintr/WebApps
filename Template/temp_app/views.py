from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import requests as req
import datetime as dt

# Create your views here.
def index(request):
    return render(request,"temp_app/first.html")

def currency(request):
    currency_dict = {"Dollar":[37.7,38.8], 
                     "Euro":[43.55,44.05], 
                     "Gold":[3890.05,3982.44], 
                     "BTC":{"Ethereum":100590.84,"Doge":9.15,"Lite":3794.85},
                     "user_pro" :  True,
                     "testing" : "TesT iS oK"
                     }

    return render(request,"temp_app/currency.html",context=currency_dict)


####################################################


def earthquake(request):
    # VARIABLES:
    start_date_year = "2025"
    start_date_month = "04"
    start_date_day = "22"
    start_date_hour = "00"
    start_date_minute = "00"
    start_date_second = "01"

    """end_date_year = "2023"
    end_date_month = "02"
    end_date_day = "06"
    end_date_hour = "23"
    end_date_minute = "59"
    end_date_second = "59" """

    now = dt.datetime.now()
    end_date_year = str(now.year)
    end_date_month = str(now.month)
    end_date_day = str(now.day)
    end_date_hour = str(now.hour)
    end_date_minute = str(now.minute)
    end_date_second = str(now.second)

    locator1 = "İstanbul"
    locator2 = "Tekirdağ"
    locator3 = "Bursa"
    locator4 = "Bolu"

    mag = 3.0
    i=0
    
    listing = []
    
    url = f"https://servisnet.afad.gov.tr/apigateway/deprem/apiv2/event/filter?start={start_date_year}-{start_date_month}-{start_date_day}%20{start_date_hour}:{start_date_minute}:{start_date_second}&end={end_date_year}-{end_date_month}-{end_date_day}%20{end_date_hour}:{end_date_minute}:{end_date_second}" #for live data

    
    response = req.get(url)
    if response.status_code == 200:   
        for query in response.json():
            if query["province"] == locator1 or query["province"]==locator2 or query["province"]==locator3 or query["province"]==locator4:
                if float(query["magnitude"])>mag:
                    i+=1
                    ##dict.update({(f"{i}"):(f"{query["date"][0:16]}")})
                    ##dict[f"a{i}"]=(f"{i} - {query["date"][0:16]}-{query["location"]}-{query["magnitude"]}--{query["depth"]}")
                    listing.append(f"{i} - {query["date"][0:16]}-{query["location"]}-{query["magnitude"]}")
    dict = {"lister":listing} 
    return render(request,"temp_app/earthquake.html",context=dict)
