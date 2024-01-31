from django.db import models


class Challenges(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()

# completed = models.ManyToManyField(
#     "Challenges", related_name="completed", blank=True
# )