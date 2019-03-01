# import asyncio
# import json
# from django.contrib.auth import get_user_model
# from channels.consumer import AsyncConsumer
# from channels.db import database_sync_to_async
#
# from src.models.profile.models import Profile
#
#
# class VideoConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("Connected ...", event)
#         await self.send({
#             "type": "websocket.accept"
#         })
#         print(self.scope['user'])
#         #await asyncio.sleep(10)
#         await self.send({
#             "type": "websocket.send",
#             "text": "Hello WORLD"
#         })
#
#     async def websocket_receive(self, event):
#         print('Receive ...', event)
#
#     async def websocket_disconnect(self, event):
#         print('Disconnected ...', event)
