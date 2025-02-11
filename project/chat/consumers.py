import json
from datetime import datetime
import urllib.parse
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.authtoken.models import Token
from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from app.models import Profile
from django.contrib.auth.models import User
from django.conf import settings

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        token = (urllib.parse.unquote(query_string.split("token=", 1)[-1].split("&")[0]).strip().replace('"', '') if "token=" in (query_string := self.scope.get("query_string", b"").decode()) else None)
        self.user = await self.get_user(token) or "Anonymous"
        self.profile = await self.get_user_profile(self.user)
        
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat.message", 
                "user": self.user,
                "profile": self.profile,
                "message": message,
                "timestamp":timestamp,
                }
            )
        
    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event["user"]
        profile = event["profile"]
        timestamp = event["timestamp"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            "user": username,
            "profile": profile,
            "timestamp":timestamp,
            }))


    async def get_user(self, token_key):
        """Retrieve user from token asynchronously. Returns None if token is invalid."""
        try:
            user_token = await sync_to_async(Token.objects.select_related("user").get, thread_sensitive=True)(key=token_key)
            username = user_token.user.username
            return username
        except ObjectDoesNotExist:
            return None
        
    async def get_user_profile(self, user):
        """Retrieve user from token asynchronously. Returns None if token is invalid."""
        try:
            user_instance = await sync_to_async(User.objects.get, thread_sensitive=True)(username=user)
            user_profile = await sync_to_async(Profile.objects.select_related("user").get, thread_sensitive=True)(user=user_instance)
            user_profile =  f"{settings.SITE_URL}{user_profile.image.url}" if user_profile.image else None#user_profile.image.url if user_profile.image else None
            return user_profile
        except ObjectDoesNotExist:
            return None