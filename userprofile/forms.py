
from django.contrib.auth import get_user_model
from django import forms


class UserChangeForm(forms.ModelForm):

    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-field'}), required=True)
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-field'}),required=False)
    phone = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'class': 'login-field'}),required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-field'}),required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-field'}),required=False)
    password1 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'login-field'}))
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'login-field'}))

    class Meta:
        model = get_user_model()
        fields = ['email', 'company_name', 'phone', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

        labels = ['Email', 'Navn på bedrift', 'Telefon', 'Fornavn', 'Etternavn', 'Nytt passord', 'Bekreft passord']
        index = 0
        for fieldname in ['email', 'company_name', 'phone', 'first_name', 'last_name', 'password1', 'password2']:
            self.fields[fieldname].error = None
            self.fields[fieldname].label = labels[index]
            index += 1