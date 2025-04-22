from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"), ## url:indlocalhost/app/
    path("<str:userurl>/", views.course, name="course"), ## url:localhost/app/cisco/
    path("<int:n1>/<int:n2>/",views.multi_view,name="multi"), ## url:localhost/app/4/8/
    path("<int:n1>",views.course_select,name="course_select")
]