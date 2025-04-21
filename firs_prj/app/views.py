from django.shortcuts import render
from django.http import HttpResponse

course_dict = {
    "python":"Welcome to Python Course",
    "cisco":"Welcome to Cisco Course",
    "java":"Java Course",
    "charp":"C# Course",
    "swift":"Swift Course"
}

def index(request):
    return HttpResponse("First Django Project Test OK.")


def course(request, userurl): #user_url: user browser written url.
    return HttpResponse(course_dict.get(userurl,"Page is Not Found - 404"))

def multi_view(request,n1,n2):
    return HttpResponse(f"{n1}^{n2}={pow(n1,n2)}")