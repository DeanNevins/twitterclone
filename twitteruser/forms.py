from django import forms
from django.forms.widgets import PasswordInput
from twitteruser.models import TwitterUser


class TwitterUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=PasswordInput)