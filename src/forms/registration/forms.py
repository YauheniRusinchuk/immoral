from django import forms


class FormRegistration(forms.Form):

    login = forms.CharField(label='',required=True,max_length=100)
    password = forms.CharField(label='',required=True,widget=forms.PasswordInput())

    login.widget.attrs.update({'placeholder': 'Login* ...', 'class' : 'registration_login_form',
                                    'autocomplete' : 'off',
    })
    password.widget.attrs.update({'placeholder': 'Password* ...', 'class' : 'registration_password_form',
                                    'autocomplete' : 'off',
    })
