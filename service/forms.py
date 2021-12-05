from django import forms
from django.forms.fields import CharField
from django.forms.forms import Form

class NameForm(forms.Form):
    name = forms.CharField(max_length = 100)