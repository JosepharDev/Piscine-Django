from django import forms

class Update_crawl(forms.Form):
    item_to_update = forms.ChoiceField(
        choices=[],
        label="Select a movie to update it's opening_crawl"
    )
    new_crawl = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        label="New Opening Crawl Content"
    )
    def __init__(self, movie_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_to_update'].choices = [("", "--- Select a Movie ---")] + movie_choices