from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from ..models.user import AppUser

class UserLoginForm(forms.Form):

    email = forms.EmailField(max_length = 255)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        self.fields['email'].widget.attrs.update({'class' : 'form-control' })
        self.fields['password'].widget.attrs.update({'class' : 'form-control' })


class UserCreationForm(forms.ModelForm):

    email = forms.EmailField(max_length = 255)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AppUser
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['email'].widget.attrs.update({'class' : 'form-control' })
        self.fields['password'].widget.attrs.update({'class' : 'form-control' })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    def __init__(self, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        self.fields['email'].widget.attrs.update({'class' : 'form-control' })

    class Meta:
        model = AppUser
        fields = ('email', 'password')
