from django.contrib.auth import authenticate, login

from .models import *
from .forms import UserForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# Create your views here.

def my_setting(request):
    return render(request, 'my_setting.html')


def join(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=raw_password)
            if user is not None:
                login(request, user)
            account.save()
            return redirect('account:login')
    else:
        form = UserForm()
    return render(request, 'join.html', {'form': form})