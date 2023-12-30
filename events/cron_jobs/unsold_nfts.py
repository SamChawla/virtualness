from django.utils import timezone
from datetime import timedelta
from events.models import Event


def alert_unsold_nfts():
    print("Alerting unsold NFTs...")
    seven_days_ago = timezone.now() - timedelta(days=7)
    unsold_nfts = Event.objects.filter(
        verb="post", timestamp__lte=int(round(seven_days_ago.timestamp()))
    )

    for nft in unsold_nfts:
        # Logic is not clear in the assignment as to how we identify the unsold NFTs
        print(f"Alert sent to seller: {nft.userid}")
