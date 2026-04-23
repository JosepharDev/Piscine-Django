from django import forms


class TextInputForm(forms.Form):
    """Form for text input with history tracking"""
    text_input = forms.CharField(
        label='Enter your text',
        max_length=100,
        min_length=5,
        widget=forms.TextInput(attrs={
            'placeholder': 'Type something here...',
            'class': 'form-input'
        })
    )
