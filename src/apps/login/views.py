from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from src.forms.login.forms import LoginForm
# Create your views here.

class Login(View):
    '''  Login page  '''
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home_page')
        else:
            form = LoginForm()
            return render(request, 'login/index.html', {"form" : form})

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
                return redirect('home:login_page')
