from django.forms import ModelForm
from . import models

class AccountForm(ModelForm):
    '''Account Form Class'''
    class Meta:
        model = models.Account
        fields = [
            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'bio',
            'avatar'
            ]
