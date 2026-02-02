from django.db import models
from django.utils import timezone
from rest_framework import serializers


class StreamingSession(models.Model):
    title = models.CharField()
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(null=True, blank=True)
    resolution_x = models.IntegerField(default=1080)
    resolution_y = models.IntegerField(default=1920)

    @property
    def active(self):
        return self.end is None

    def __str__(self):
        return self.title


class StreamingSessionSerializer(serializers.ModelSerializer):
    active = serializers.SerializerMethodField("get_active")

    class Meta:
        model = StreamingSession
        fields = "__all__"
        read_only_fields = ["start", "end"]

    def get_active(self, session: StreamingSession):
        return session.active
