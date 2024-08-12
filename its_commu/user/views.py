from django.shortcuts import render

# Create your views here.

def my_setting(request):
    return render(request, 'my_setting.html')

def join(request):
    return render(request, 'join.html')