from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField( max_length=100)
    website = models.URLField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyine = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)