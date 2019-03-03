# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
# from src.models.posts.models import Post
#
# @receiver(post_save, sender=Post)
# def announce_new_user(sender, instance, created, **kwargs):
#     print("SIGNAL")
#     if created:
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             "gossip", {"type": "user.gossip",
#                        "event": "New User",
#                        })
