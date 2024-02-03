from django.db import models


class Challenges(models.Model):
    title = models.CharField(max_length=100, unique=True)
    full_title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    week = models.IntegerField(default=0)
    author = models.CharField(max_length=100, default="")  # Typically Thomas: Not sure we should track this data as it's PII
    topics = models.JSONField(null=True)


class Courses(models.Model):
    name = models.CharField(max_length=16, null=True, default="CS50x")
    problems = models.ManyToManyField(Challenges, related_name="courses", null=True)

    def __str__(self):
        return self.name

# completed = models.ManyToManyField(
#     "Challenges", related_name="completed", blank=True
# )

