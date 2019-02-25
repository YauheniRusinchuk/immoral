from django.shortcuts import render, redirect, Http404, reverse
from django.views import View
from src.models.profile.models import Profile
from django.contrib.auth.models import User


class ProfileDetail(View):
    ''' View Profile Detail page  '''
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
            return render(request, 'profile/settings.html', {'profile': profile})
        else:
            return redirect('home:home_page')

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        user.username = request.POST.get('login')
        profile = Profile.objects.get(user=user)
        avatar = profile.img
        try:
            user.save()
            if request.FILES:
                profile.img = request.FILES['file']
            else:
                profile.img = avatar
        except Exception:
            return redirect('home:settings_page', slug=profile.slug)
        profile.description = request.POST.get('description')
        profile.save()
        return redirect('home:profile_page', slug=profile.slug)
