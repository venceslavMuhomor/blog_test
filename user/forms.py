from django import forms
from django.contrib.auth import get_user_model
from django.forms import SelectDateWidget

from .models import Account


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'avatar_image', 'gender')
        widgets = {
            'birth_date': SelectDateWidget(years=range(1980, 2030))
        }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('пароли не совпадают.')
        return cd['password2']


class ChangeUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'birth_date', 'avatar_image', 'gender')
        widgets = {
            'birth_date': SelectDateWidget(years=range(1980, 2030))
        }