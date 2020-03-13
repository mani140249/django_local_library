from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver

from .models import Student, Organizer


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff and not instance.is_superuser:
            Organizer.objects.create(user=instance)
        elif not instance.is_staff:
            Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if instance.is_staff and not instance.is_superuser:
        instance.organizer.idno = instance.username
        instance.organizer.save()
        organizer_group = Group.objects.get(name='organizer')
        organizer_group.user_set.add(instance)
        
    elif not instance.is_staff:
        instance.student.idno = instance.username
        instance.student.save()
