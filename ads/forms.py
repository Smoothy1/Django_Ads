from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class AddAdForms(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['cat'].empty_label = 'Заполните категорию'

    class Meta:
        model = Ads
        fields = ['name', 'slug', 'year', 'price', 'photo', 'cat']

    def clean_year(self):
        year = self.cleaned_data['year']
        if year > 2023:
            raise ValidationError(f'{year} год еще не наступил')
        return year


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))



