from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse
import os


class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, primary_key = True)
    description = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='ava_profile/', blank=True, null=True)
    is_offical = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('home:profile_page', kwargs={'slug' : self.slug})

    def get_absolute_url_settings(self):
        return reverse('home:settings_page', kwargs={'slug': self.slug})


    def __str__(self):
        return f"{self.user} Profile"




def pre_save_profile_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.user)
    instance.slug = slug
    if not instance.img:
         return False
    old_file = sender.objects.get(user=instance.user).img or None

    if old_file:
        if not old_file == instance.img:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)





pre_save.connect(pre_save_profile_receiver, sender=Profile)
