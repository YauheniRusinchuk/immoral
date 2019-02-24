from django.shortcuts import render, redirect
from django.views import View
from src.models.profile.models import Profile


class ProfileDetail(View):
    def get(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(slug=kwargs['slug'])
        except Exception:
            return redirect('home:home_page')
        print(profile)    
        return render(request, 'profile/index.html', {})
