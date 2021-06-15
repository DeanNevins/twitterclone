from django.db import models
from django.utils import timezone

from twitteruser.models import TwitterUser
# Create your models here.

class Tweet(models.Model):
    tweet = models.TextField(max_length=140)
    poster = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.id} - {self.tweet}'