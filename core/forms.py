
from django import forms
from .models import NewsLetterSubscription


class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewsLetterSubscription
        fields = ['email']