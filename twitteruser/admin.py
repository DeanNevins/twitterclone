from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from twitteruser.models import TwitterUser
# Register your models here.
UserAdmin.fieldsets[1][1]['fields'] += ('following',)

admin.site.register(TwitterUser, UserAdmin)