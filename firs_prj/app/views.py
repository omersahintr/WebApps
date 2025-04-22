from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

course_dict = {
    "python":"Welcome to Python Course",
    "cisco":"Welcome to Cisco Course",
    "java":"Java Course",
    "charp":"C# Course",
    "swift":"Swift Course"
}

def index(request):
    return HttpResponse("First Django Project Test OK.")


##def course(request, userurl): #user_url: user browser written url.
    ##return HttpResponse(course_dict.get(userurl,"Page is Not Found - 404"))

def multi_view(request,n1,n2):
    return HttpResponse(f"{n1}^{n2}={pow(n1,n2)}")

def course(request,userurl):
    try:
        course = course_dict[userurl]
        return HttpResponse(course)
    except:
        
        raise Http404("404 - This page is not found!")
    
def course_select(request,n1): ##localhost/1/ --> localhost/cisco/
    course_list = list(course_dict.keys()) ##get dictionary id's
    try:
        course = course_list[n1]
        page = reverse("course", args=[course]) ##select urls.py paths name parameters
        return HttpResponseRedirect(page)
    except:
        raise Http404("404 - This page is not found!")
