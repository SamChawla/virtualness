from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate
from django.urls import reverse
from events.models import Event
from events.serializers import EventSerializer


class EventViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.event_data = {
            "userid": self.user.id,
            "verb": "buy",
            "noun": "nft",
            "timestamp": 1656613800,
            "properties": {
                "mode": "netbank",
                "bank": "hdfc",
                "merchantid": 234,
                "value": 4500,
                "currency": "INR",
            },
        }

    def test_create_event(self):
        url = reverse("event-view")
        self.client.force_authenticate(user=self.user, token=self.token)

        response = self.client.post(url, self.event_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        event = Event.objects.get(pk=response.data["id"])
        serializer = EventSerializer(event)
        self.assertEqual(response.data["properties"], serializer.data["properties"])

    def test_failed_event(self):
        url = reverse("event-view")
        self.client.force_authenticate(user=self.user, token=self.token)

        response = self.client.post(url, {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
