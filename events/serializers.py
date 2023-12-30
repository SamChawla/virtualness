from events.models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["userid", "verb", "noun", "timestamp", "properties"]

        extra_kwargs = {
            "userid": {"required": True},
            "verb": {"required": True},
            "noun": {"required": True},
            "timestamp": {"required": True},
            "properties": {"required": True},
        }
