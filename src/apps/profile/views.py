from django.shortcuts import render
from django.views import View



class ProfileDetail(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile/index.html', {})
