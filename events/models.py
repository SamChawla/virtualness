from enum import Enum
from django.db import models
from django.contrib.auth.models import User


class VerbChoices(Enum):
    BUY = "buy"
    POST = "post"


class NounChoices(Enum):
    NFT = "nft"
    FEEDBACK = "feedback"


class Event(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    verb = models.CharField(
        max_length=10, choices=[(choice.value, choice.name) for choice in VerbChoices]
    )
    noun = models.CharField(
        max_length=10, choices=[(choice.value, choice.name) for choice in NounChoices]
    )
    timestamp = models.BigIntegerField()
    properties = models.JSONField()

    def __str__(self):
        return f"Event {self.pk}: {self.verb} {self.noun} by User {self.userid}"
