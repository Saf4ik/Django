from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AccountLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=128, required=True
    )
    password = forms.CharField(
        max_length=72, required=True,
        widget=forms.widgets.PasswordInput()
    )