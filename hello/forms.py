from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *


class FormOrder(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    class Meta:
        model = Order
        fields = ['customer_name', 'customer_mail', 'customer_phone']

    def clean_year(self):
        pass

