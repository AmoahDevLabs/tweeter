from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance, slug=instance.username)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()
