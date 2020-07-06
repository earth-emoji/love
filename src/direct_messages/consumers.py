import asyncio
import json

from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.shortcuts import redirect, reverse

from .models import Channel, ChannelMessage
from users.models import User

class MessageConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connect", event)

        user = self.scope['user']
        if user.is_authenticated:
            await self.send({
                'type':'websocket.accept',
            })

            # get user and room
            # self.profile = UserProfile.objects.get(user=user)
            
            self.channel_id = self.scope['url_route']['kwargs']['pk']

            self.channel = Channel.objects.get(id=self.channel_id)
            
            await self.channel_layer.group_add(
                    self.channel_id,
                    self.channel_name
            )

            await self.send({
                "type": "websocket.send",
                "text": self.channel_id
            })

    async def websocket_receive(self, event):
            print("receive", event)
            text = event.get('text', None)

            if text is not None:
                loaded_data = json.loads(text)
                msg = loaded_data.get('message')
                user = self.scope['user']

                if user.is_authenticated:
                    json_response = {
                        'message': msg,
                        'username': user.username
                    }

                    # save to database
                    await self.create_message(msg)

                    # broadcast data back to client
                    await self.channel_layer.group_send(
                        self.channel_id,
                        {
                            "type": "chat_message",
                            "text": json.dumps(json_response)
                        }
                    )

    async def chat_message(self, event):
        # send the actual message
        print("message", event)
        await self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    async def websocket_disconnect(self, event):
        print("disconnect", event)

    @database_sync_to_async
    def create_message(self, msg):
        user = self.scope['user']
        return ChannelMessage.objects.create(user=user, content=msg, channel=self.channel)


