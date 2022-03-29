from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    important = models.BooleanField()
    urgent = models.BooleanField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
