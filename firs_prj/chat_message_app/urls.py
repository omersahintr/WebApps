from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"), ## url:index 
    ##path("contacts",views.index, name="index") ## url:/contacts

    path("cisco/", views.cisco_course, name="cisco"),
    path("python/", views.python_course, name="Python")
    
]