from django.forms import (EmailField, ModelForm, ValidationError,
                          CharField, HiddenInput)
from .models import Account

class AccountForm(ModelForm):
    '''Account Form Class'''
    email_confirmation = EmailField(required=True)

    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'email',
            'email_confirmation',
            'date_of_birth',
            'bio',
            'avatar'
            ]

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get('email')
        email_confirmation = cleaned_data.get('email_confirmation')
        if email != email_confirmation:
            raise ValidationError("Emails must match")
            
        bio = cleaned_data.get('bio')
        if len(bio) < 10:
            raise ValidationError("The bio must be at least ten characters")
