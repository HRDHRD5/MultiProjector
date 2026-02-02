from urllib.parse import parse_qs
from django.shortcuts import render
from django.http import HttpRequest
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.typing import WebSocketConnectEvent, WebSocketCloseEvent, WebSocketReceiveEvent
from rest_framework import viewsets, permissions, decorators, response
from streaming.models import StreamingSession, StreamingSessionSerializer


class ReadAndCreate(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return request.method in permissions.SAFE_METHODS + ("POST",)


class ProjectorStream(AsyncWebsocketConsumer):
    async def websocket_connect(self, event: WebSocketConnectEvent):
        try:
            stream_id = parse_qs(dict(self.scope)["query_string"].decode())["stream"][-1]
            stream = await database_sync_to_async(StreamingSession.objects.get)(pk=stream_id)
            print(stream)
            await self.accept()
        except Exception:
            await self.close()

    async def websocket_disconnect(self, event: WebSocketCloseEvent):
        await self.close()

    async def websocket_receive(self, event: WebSocketReceiveEvent):
        await self.send(text_data="error")


class StreamingSessionViewSet(viewsets.ModelViewSet):
    queryset = StreamingSession.objects.order_by(
        "start").filter(end=None).distinct()
    serializer_class = StreamingSessionSerializer
    permission_classes = [ReadAndCreate]
