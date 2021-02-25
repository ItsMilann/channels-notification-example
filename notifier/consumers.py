from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.consumer import AsyncConsumer
import asyncio


class NotificationConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("notification", self.channel_name)
        print(f"Added {self.channel_name} channel to gossip")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notification", self.channel_name)
        print(f"Removed {self.channel_name} channel to gossip")

    async def new_notification(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")

    '''
    Inherit AsyncConsumer
    
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })
    '''
    # async def connect(self):
    #     await self.accept()
    #     while True:
    #         await asyncio.sleep(1)
    #         await self.send_json("Tick")
    #         await asyncio.sleep(1)
    #         await self.send_json("....Tock")
