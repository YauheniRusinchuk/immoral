from django.shortcuts import render
from django.views import View
from src.models.profile.models import Profile
from src.models.posts.models import Post
# Create your views here.



class Home(View):
    ''' Home page view  '''
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {"posts": posts})
