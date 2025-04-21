from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("First Django Project Test OK.")


def cisco_course(request):
    return HttpResponse("Network Cisco Course")

def python_course(request):
    return HttpResponse("Python Course")
