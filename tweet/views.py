from django.shortcuts import render, HttpResponseRedirect, reverse

from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification
# Create your views here.

def tweet_add(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                tweet=data['tweet'],
                poster= request.user
            )
            users = TwitterUser.objects.all()
            for user in users:
                tag = f'@{user.username}'
                if tag in new_tweet.tweet:
                    Notification.objects.create(
                        recipient=user,
                        tweet=new_tweet,
                    )
            return HttpResponseRedirect(reverse('homepage'))
    
    form = TweetForm()
    return render(request, 'generic_form.html', {'form': form})


def tweet_detail(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})