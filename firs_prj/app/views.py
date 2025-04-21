from django.shortcuts import render
from django.http import HttpResponse

course_dict = {
    "python" : "Welcome to Python Course",
    "cisco" : "Welcome to Cisco Course",
    "java"  : "Java Course",
    "charp" : "C# Course",
    "swift" : "Swift Course"
}

def index(request):
    return HttpResponse("First Django Project Test OK.")


def select_course(request, user_url): #user_url: user browser written url.
    return HttpResponse(course_dict[user_url])
