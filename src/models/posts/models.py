from django.db import models
from django.db.models.signals import pre_delete, post_save
from src.models.profile.models import Profile
from datetime import datetime
from django.shortcuts import reverse
import os
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=False)
    date_create = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home:detail_post', kwargs={'slug' : self.profile.slug, 'pk': self.pk})


    class Meta:
        ordering = ['-date_create']

    def __str__(self):
        return f"this is post profile {self.profile.user}"


class Img(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/')



def post_save_update(sender, instance, *args, **kwargs):
    if instance.save:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "newpost", {"type": "user.gossip",
                        "event": "New User",
                        })



def post_delete_img(sender, instance, *args, **kwargs):
    img = Img.objects.filter(post=instance)
    if img is None:
        return False
    if img:
        for i in img:
            if os.path.isfile(i.img.path):
                os.remove(i.img.path)


post_save.connect(post_save_update, sender=Post)
pre_delete.connect(post_delete_img, sender=Post)
