from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from ..models.user import AppUser

class BaseForm(forms.Form):
    pass

class AccountStartStep1(BaseForm):

    __CHOICES__ = [
        ('owner', 'propriétaire'),
        ('employee', 'employé'),
    ]

    type = forms.ChoiceField(choices=__CHOICES__, widget=forms.RadioSelect)

    def __processing_create__(self, request, data, message, instance):
        if request.method == 'POST':
            form = AccountStartStep1(request.POST)
        else:
            form = AccountStartStep1()
        data = {}
        data['form'] = form
        data['back'] = ''
        data['next'] = ''
        return render(request, 'accounts/wizard.html', data)
