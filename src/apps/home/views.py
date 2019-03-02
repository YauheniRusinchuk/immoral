from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from src.models.profile.models import Profile
from src.models.posts.models import Post, Img
# Create your views here.



class Home(View):
    ''' Home page view  '''
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {"posts": posts})


class PlusNew(View):
    ''' Add new post '''
    def post(self, request, *args, **kwargs):
        post = Post(profile=request.user.profile, text=request.POST.get('text'))
        post.save()
        for f in request.FILES.getlist('img'):
            media = Img(post=post, img=f)
            media.save()
        return HttpResponseRedirect('/')
