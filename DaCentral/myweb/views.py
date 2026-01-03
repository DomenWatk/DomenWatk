from django.shortcuts import HttpResponse,render

import datetime

# Create your views here.
def home(request):
    current_year=datetime.datetime.now().year
    return render(request,"Temp.html",{"year":current_year})
def nav(request):
    return render(request,"Nav.html")
def signup(request):
    return render(request,"signup.html")
def signin(request):
    return render(request,"signin.html")
def footer(request):
    return render(request,"Footer.html")