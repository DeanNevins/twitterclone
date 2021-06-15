from django import forms

from tweet.models import Tweet

class TweetForm(forms.Form):
    tweet = forms.CharField(widget=forms.Textarea(attrs={'class': 'nes-textarea'}),max_length=140)