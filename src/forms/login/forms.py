from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="",required=True,max_length=100)
    password = forms.CharField(label="",required=True,widget=forms.PasswordInput())

    username.widget.attrs.update({'placeholder': 'Username ...'})
    password.widget.attrs.update({'placeholder': 'Password ...'})
