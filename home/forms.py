# home/forms.py
from django import forms

class GirlfriendLoginForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "placeholder": "Your name",
        "class": "input"
    }))
    anniversary = forms.DateField(widget=forms.DateInput(attrs={
        "type": "date",
        "class": "input"
    }))
