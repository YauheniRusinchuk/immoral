from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views import View
from src.models.profile.models import Profile

class Registration(View):
    ''' Registration view  '''
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home_page')
        return render(request, 'registration/index.html', {})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = User(username=username)
        user.set_password(password)
        try:
            user.save()
        except Exception:
            return HttpResponse('error python')
        profile = Profile(user=user)
        profile.save()
        return HttpResponse('success...')
