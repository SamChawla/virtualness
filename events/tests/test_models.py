from django.test import TestCase
from events.models import Event
from django.utils import timezone
from django.contrib.auth.models import User


class EventTest(TestCase):
    def create_event(
        self,
        verb="buy",
        noun="nft",
        timestamp=int(round(timezone.now().timestamp())),
        properties={},
    ):
        user = User.objects.create(username="testuser", password="testpass")
        return Event.objects.create(
            userid=user,
            verb=verb,
            noun=noun,
            timestamp=timestamp,
            properties=properties,
        )

    def test_event_creation(self):
        event = self.create_event()
        print(event)
        self.assertTrue(isinstance(event, Event))
