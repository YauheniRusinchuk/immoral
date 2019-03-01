from django.db import models
from src.models.profile.models import Profile


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return f"this is post profile {self.profile.user}"
