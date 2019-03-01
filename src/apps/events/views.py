from django.shortcuts import render, redirect
from django.views import View
from src.models.profile.models import Profile

class Events(View):
    ''' Events page  '''
    def get(self, request, *args, **kwargs):
        return render(request, 'events/index.html', {})
