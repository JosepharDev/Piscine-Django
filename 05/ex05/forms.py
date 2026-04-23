from django import forms
from .models import Movies
class MovieForm(forms.Form):
    item_to_delete = forms.ModelChoiceField(
        queryset=Movies.objects.all(),
        label="Select a movie to delete",
        empty_label="Choose a movie",
    )