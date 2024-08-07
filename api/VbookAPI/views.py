from django.shortcuts import render
from django.http import HttpResponse

# def Vbook_api(request):
#     return HttpResponse("Hello world!")
def get_home(request):
    return render(request,'Vbook_web/home.html')
def get_login(request):
    return render(request,'Vbook_web/login.html')