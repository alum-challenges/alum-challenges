from django.contrib.auth.models import AbstractUser
from django.db import models


class Challenges(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

# completed = models.ManyToManyField(
#     "Challenges", related_name="completed", blank=True
# )