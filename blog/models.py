from django.db import models
import datetime


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.title
