from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.


class Registration(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    user_Id = models.CharField(max_length=50)
    mobileNumber = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)