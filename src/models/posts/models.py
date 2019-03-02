from django.db import models
from django.db.models.signals import pre_delete
from src.models.profile.models import Profile
from datetime import datetime
import os

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=False)
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_create']

    def __str__(self):
        return f"this is post profile {self.profile.user}"


class Img(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/')



def post_delete_img(sender, instance, *args, **kwargs):
    img = Img.objects.filter(post=instance)
    print(img)
    if img is None:
        return False
    if img:
        for i in img:
            if os.path.isfile(i.img.path):
                os.remove(i.img.path)



pre_delete.connect(post_delete_img, sender=Post)
