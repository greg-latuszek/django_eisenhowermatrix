from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    important = models.BooleanField()
    urgent = models.BooleanField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
