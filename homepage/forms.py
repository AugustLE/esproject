from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserLoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login-field'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-field'}))

    class Meta:
        model = get_user_model()
        fields = ['email','password']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

        labels = ["Email", "Passord"]
        index = 0
        for fieldname in ['email', 'password']:
            self.fields[fieldname].label = labels[index]
            index += 1


class UserSignupForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login-field'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login-field'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-field'}))

    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        labels = ["Email", "Passord", "Bekreft passord"]
        index = 0
        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = labels[index]
            index += 1
