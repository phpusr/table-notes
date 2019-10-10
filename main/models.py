from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class OwnerModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True
