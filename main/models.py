from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    friends = models.ManyToManyField('self', blank=True)


class OwnerModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')

    class Meta:
        abstract = True
