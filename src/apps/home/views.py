from django.shortcuts import render
from django.views import View
from src.forms.login.forms import LoginForm
# Create your views here.



class Home(View):
    ''' Home page view  '''
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'home/index.html', {})
        else:
            form = LoginForm()
            return render(request, 'home/index.html', {'form': form})
