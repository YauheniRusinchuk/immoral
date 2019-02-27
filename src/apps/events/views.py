from django.shortcuts import render
from django.views import View

class Events(View):
    ''' Events page  '''

    def get(self, request, *args, **kwargs):
        return render(request, 'events/index.html', {})
