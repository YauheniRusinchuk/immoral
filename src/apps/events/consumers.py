from channels.generic.websocket import AsyncJsonWebsocketConsumer,WebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
import json
from src.models.posts.models import Post
from src.models.comments.models import Comment


class PostConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("newpost", self.channel_name)
        print(f"Added {self.channel_name} channel to new post")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("newpost", self.channel_name)
        print(f"Removed {self.channel_name} channel to new post")

    async def user_gossip(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")



class CommentCunsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        pk_post = self.scope['url_route']['kwargs']['pk']
        post = Post.objects.get(pk=pk_post)
        self.post = post
        self.pk_post = "id" + str(pk_post)
        await self.channel_layer.group_add(
            self.pk_post,
            self.channel_name,
        )
        await self.send({
            "type": "websocket.accept",
        })
        print("SOCKET MSG ...")

    async def websocket_receive(self, event):
        print('receive ...')
        text_comment = event.get('text', None)
        if text_comment is not None:
            load_data = json.loads(text_comment)
            message = load_data.get('message')
            user = self.scope['user']
            url_img = ""
            if user.profile.img:
                url_img = user.profile.img.url
            response = {
                'message': message,
                'username': user.username,
                'url_img': url_img,
                'url_profile': user.profile.get_absolute_url(),
            }
            await self.create_comment(user, message)
            await self.channel_layer.group_send(
                self.pk_post,
                {
                    "type": "msg_post",
                    "text": json.dumps(response),
                }
            )

    async def msg_post(self, event):
        #print('message', event)
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })

    @database_sync_to_async
    def create_comment(self, user, msg):
        Comment.objects.create(profile=user.profile, text=msg, post=self.post)


    async def websocket_disconnect(self, event):
        print("disconnect")
