from django.db import models
from src.models.profile.models import Profile
from src.models.posts.models import Post

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment for post is {self.post.pk}"
