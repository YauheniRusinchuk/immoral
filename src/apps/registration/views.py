from django.shortcuts import render, redirect, HttpResponse, Http404
from django.contrib.auth.models import User
from django.views import View
from src.models.profile.models import Profile
from src.forms.registration.forms import FormRegistration

class Registration(View):
    ''' Registration view  '''
    def get(self, request, *args, **kwargs):
        form = FormRegistration()
        if request.user.is_authenticated:
            return redirect('home:home_page')
        return render(request, 'registration/index.html', {'form' : form})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = User(username=username)
        user.set_password(password)
        try:
            user.save()
        except Exception:
            return Http404()
        profile = Profile(user=user)
        profile.save()
        return HttpResponse('success...')
