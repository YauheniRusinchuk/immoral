from channels.generic.websocket import AsyncJsonWebsocketConsumer,WebsocketConsumer
from channels.consumer import AsyncConsumer
import json
from channels.auth import get_user

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
            response = {
                'message': message,
                'username': user.username,
            }
            await self.send({
                "type": "websocket.send",
                "text": json.dumps(response),

            })

    async def websocket_disconnect(self, event):
        print("disconnect")
