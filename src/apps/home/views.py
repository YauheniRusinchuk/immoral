from django.shortcuts import render
from django.views import View
from src.models.profile.models import Profile
# Create your views here.



class Home(View):
    ''' Home page view  '''
    def get(self, request, *args, **kwargs):
        return render(request, 'home/index.html', {})
