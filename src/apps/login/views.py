from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from src.forms.login.forms import LoginForm
# Create your views here.

class Login(View):
    ''' Check Login and '''
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:home_page')
            else:
                print('Error login')
                return redirect('home:home_page')
    
