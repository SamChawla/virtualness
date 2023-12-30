from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event


@receiver(post_save, sender=Event)
def send_push_notification(sender, instance, created, **kwargs):
    if (
        created
        and instance.verb == "buy"
        and sender.objects.filter(verb="buy", userid=instance.userid).count() == 1
    ):
        print("Sending push notification to user...")


@receiver(post_save, sender=Event)
def alert_operator(sender, instance, created, **kwargs):
    if created and instance.verb == "buy":
        one_hour_ago = timezone.now() - timedelta(hours=1)
        purchased_nfts = Event.objects.filter(
            verb="buy",
            userid=instance.userid,
            timestamp__gte=int(round(one_hour_ago.timestamp())),
        )
        if purchased_nfts.count() > 100:
            # Add Logic to alert the operator
            print("Condition satisfied! Printing function...")
