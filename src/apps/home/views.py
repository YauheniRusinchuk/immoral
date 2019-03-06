from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.db.models import Q
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



class DetailPost(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        return render(request, 'posts/detail.html', {'post': post})



class Search(View):
    ''' Search page  '''
    def get(self, request, *args, **kwargs):
        query:str = request.GET.get('q')
        if query:
            posts:list = Post.objects.filter(
                Q(text__icontains=query) |
                Q(text__startswith=query) |
                Q(text__istartswith=query) |
                Q(text__endswith=query) |
                Q(text__iendswith=query)
            )
            print(posts)
            return render(request, 'search/search.html', {'posts': posts})
        return redirect('home:home_page')
