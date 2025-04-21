from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"), ## url:index 
    ##path("contacts",views.index, name="index") ## url:/contacts

    path("<str:user_url>/", views.select_course, name="course")
    
]