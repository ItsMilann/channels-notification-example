from channels.layers import get_channel_layer
from django.db import models
from django.db.models.signals import post_save


class Notifications(models.Model):
    text = models.CharField(
        max_length=255, default="You have been kicked out of the clan.")

    def __str__(self):
        return self.text


def notification_receiver(sender, instance, created, *args, **kwargs):
    from asgiref.sync import async_to_sync
    if created:
        print("IF RAN")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notification", {
                "type": "new.notification",
                "event": "Notification",
                "text": instance.text
            })


post_save.connect(notification_receiver, sender=Notifications)
