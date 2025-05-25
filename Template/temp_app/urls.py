from django.urls import path
from . import views

app_name = "temp_app"

urlpatterns = [
    path("",views.index,name="index"),
    path("currency/",views.currency,name="currency"),
    path("earthquake/",views.earthquake,name="earthquake")

]