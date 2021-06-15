"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import authenticate
from django.urls import path

from authentication import views as auth_views
from twitteruser import views as user_views
from tweet import views as tweet_views
from notification import views as notification_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.index, name='homepage'),
    path('notifications/', notification_views.notification),
    path('login/', auth_views.login_view, name='login_view'),
    path('logout/', auth_views.logout_view, name='logout_view'),
    path('signup/', user_views.user_add, name='signup'),
    path('tweet/add/', tweet_views.tweet_add, name='tweet_add'),
    path('tweet/<int:tweet_id>/', tweet_views.tweet_detail),
    path('<str:user_name>/', user_views.user_detail, name='user_detail'),
    path('<str:user_name>/follow/', user_views.user_follow),
    path('<str:user_name>/unfollow/', user_views.user_unfollow),
]
