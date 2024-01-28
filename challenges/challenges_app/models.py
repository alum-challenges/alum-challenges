from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True)
    completed = models.ManyToManyField(
        "Challenges", related_name="completed", blank=True
    )


class Challenges(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
