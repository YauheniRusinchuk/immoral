from channels.generic.websocket import AsyncJsonWebsocketConsumer,WebsocketConsumer
from channels.consumer import AsyncConsumer

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
        print("BLABLA", event['text'])
        print('KWARGS', self.scope)

    async def websocket_disconnect(self, event):
        print("disconnect")
