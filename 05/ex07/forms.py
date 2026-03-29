from django import forms
from .models import Movies
class update_op(forms.Form):
    drop_down = forms.ModelChoiceField(
        queryset=Movies.objects.all(),
        label="Select a movie to update",
        empty_label="Choose a movie",
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        label="New Opening Crawl Content"
    )