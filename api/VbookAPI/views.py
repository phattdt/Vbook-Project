from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

def data_view(request):
    data = MyModel.objects.all()  # Lấy tất cả các bản ghi từ MyModel
    return render(request, 'myapp/data_template.html', {'data': data})
def get_home(request):
    return render(request,'Vbook_web/home.html')
def get_login(request):
    return render(request,'Vbook_web/login.html')