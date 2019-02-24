from django.shortcuts import render, redirect
from django.views import View
from src.models.profile.models import Profile


class ProfileDetail(View):
    def get(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(slug=kwargs['slug'])
        except Exception:
            return redirect('home:home_page')
        return render(request, 'profile/index.html', {'profile': profile})


class SettingsProfile(View):
    ''' Settings profile  '''

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(slug=kwargs['slug'])
        if request.user == profile.user:
            return render(request, 'profile/settings.html', {})
        else:
            return redirect('home:home_page')    
