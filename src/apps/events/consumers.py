from channels.generic.websocket import AsyncJsonWebsocketConsumer,WebsocketConsumer


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
