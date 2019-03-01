from django.db import models
from src.models.profile.models import Profile
from datetime import datetime

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=False)
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_create']

    def __str__(self):
        return f"this is post profile {self.profile.user}"
