from django.shortcuts import render, HttpResponseRedirect, HttpResponse ,reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from twitteruser.models import TwitterUser
from twitteruser.forms import TwitterUserForm
from tweet.models import Tweet

# Create your views here.

def user_add(request):
    if request.method == "POST":
        form = TwitterUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newuser = TwitterUser.objects.create_user(username=data['username'], password=data['password'])
            login(request, newuser)
            return HttpResponseRedirect(reverse('homepage'))
    
    form = TwitterUserForm()
    return render(request, 'generic_form.html', {'form': form})
    

def user_detail(request, user_name: str):
    user = TwitterUser.objects.get(username=user_name)
    tweets = Tweet.objects.filter(poster=user.id).order_by('-post_date')
    following = user.following.all()
    if TwitterUser.objects.filter(username=request.user):
        current_user_following = request.user.following.all()
    else:
        current_user_following = None
    return render(request, 'user_detail.html', {
        'user': user,
        'tweets': tweets,
        'following': following,
        'current_user_following': current_user_following,
    })

@login_required
def user_follow(request, user_name: str):
    user = TwitterUser.objects.get(username=user_name)
    request.user.following.add(user)
    request.user.save()
    return HttpResponseRedirect(reverse('user_detail', args=(user_name,)))


@login_required
def user_unfollow(request, user_name: str):
    user = TwitterUser.objects.get(username=user_name)
    request.user.following.remove(user)
    request.user.save()
    return HttpResponseRedirect(reverse('user_detail', args=(user_name,)))