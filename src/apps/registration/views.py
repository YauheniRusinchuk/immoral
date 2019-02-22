from django.shortcuts import render, redirect
from django.views import View


class Registration(View):
    ''' Registration view  '''

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home_page')
        return render(request, 'registration/index.html', {})
