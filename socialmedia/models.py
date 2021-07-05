from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils import timezone


class User(AbstractUser):

    def uploadAvatar(instance, filename):
        username = instance.username
        ext = filename.split('.')[-1]
        formatted_time = timezone.localtime(timezone.now()).strftime('%Y%m%d%H%M%S')
        return f'profile/avatar/{username}{formatted_time}.{ext}'

    avatar = models.ImageField("Avatar", blank=True, null=True, upload_to=uploadAvatar)
    bio = models.CharField("Bio", blank=True, max_length=220)
    is_verified = models.BooleanField("Verified?", default=False)

    class Meta:
        verbose_name = "User"
        ordering = ('-id', )

    def __str__(self):
        return self.username