from django.shortcuts import render
from django.http import HttpRequest
from channels.generic.websocket import WebsocketConsumer
from rest_framework import viewsets, permissions, decorators, response
from streaming.models import StreamingSession, StreamingSessionSerializer


class ReadAndCreate(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return request.method in permissions.SAFE_METHODS + ("POST",)

class ProjectorStream(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.close()

    def receive(self, binary_data):
        self.send(text_data="error")


class StreamingSessionViewSet(viewsets.ModelViewSet):
    queryset = StreamingSession.objects.filter(end=None).distinct()
    serializer_class = StreamingSessionSerializer
    permission_classes = [ReadAndCreate]
