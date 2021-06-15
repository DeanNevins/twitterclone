from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from authentication.forms import LoginForm
from twitteruser.models import TwitterUser
from tweet.models import Tweet
# Create your views here.

@login_required
def index(request):
    current_user = TwitterUser.objects.filter(username=request.user)
    following = current_user.first().following.all()
    posters = current_user | following
    tweets = Tweet.objects.filter(poster__in=posters).order_by('-post_date')
    return render(request, "index.html", {
        'current_user': current_user,
        'tweets': tweets,
        })


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    
    form = LoginForm()
    return render(request, "generic_form.html", {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))