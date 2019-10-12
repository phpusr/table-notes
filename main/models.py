from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    friends = models.ManyToManyField('self', blank=True)


class OwnerModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')

    class Meta:
        abstract = True


class NameOwnerUniqueModel(OwnerModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class NameOwnerModel(OwnerModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        unique_together = [
            ['owner', 'name']
        ]
