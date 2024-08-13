from django.shortcuts import render, redirect
from django.contrib import auth


# Create your views here.

def my_setting(request):
    return render(request, 'my_setting.html')

def join(request):
    return render(request, 'join.html')

#로그인
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, "login_error.html")
    else:
        return render(request, "base.html")


