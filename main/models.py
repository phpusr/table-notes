from django.contrib.auth.models import User
from django.db import models


class OwnerModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True
