from django import forms

from tweets.models import Tweet


class TweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={'placeholder': 'Tweet something...', 'class': 'textarea is-info is-medium'}), label='', )

    class Meta:
        model = Tweet
        fields = ['body']
        exclude = ('user',)
