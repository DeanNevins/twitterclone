from django.db import models

from tweet.models import Tweet
from twitteruser.models import TwitterUser

# Create your models here.

class Notification(models.Model):
    recipient = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.tweet.tweet}'
