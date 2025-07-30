from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyine = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name="watchlist", null=True
    )


class Review(models.Model):
    reating = models.PositiveBigIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    reviewText = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    watchList = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='review', null=True)
