from django.db import models


class Challenges(models.Model):
    title = models.CharField(max_length=100, unique=True)
    full_title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    course = models.CharField(max_length=100, null=True, default="CS50x")
    week = models.IntegerField(default=0)
    author = models.CharField(max_length=100, default="")
    topics = models.JSONField(null=True)


# completed = models.ManyToManyField(
#     "Challenges", related_name="completed", blank=True
# )

