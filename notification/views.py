from django.shortcuts import render, HttpResponse

from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification
# Create your views here.


def notification(request):
    current_user = request.user
    notifications = None
    if current_user:
        notifications = Notification.objects.filter(recipient=current_user, seen=False).order_by('-id')
        for notification in notifications:
            notification.seen = True
            notification.save()
    return render(request, 'notification.html', {'notifications': notifications})
