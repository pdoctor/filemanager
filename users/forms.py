from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username', required=True)
    password = forms.CharField(max_length=50, label='Password', required=True, widget=forms.PasswordInput)
