from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("currency/",views.currency,name="currency"),
    path("earthquake/",views.earthquake,name="earthquake")

]