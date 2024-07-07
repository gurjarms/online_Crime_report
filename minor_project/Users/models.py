from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class UserVarify(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=50)

    def __str__(self) -> str:
        return 'user'


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pics', blank=True)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 800:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class UserMobileNo(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    Mobile = models.CharField(max_length=50)
