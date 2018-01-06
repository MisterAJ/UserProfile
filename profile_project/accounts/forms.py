import re
from django.contrib.auth.forms import PasswordChangeForm
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


class PasswordForm(PasswordChangeForm):
    username = CharField(required=False, widget=HiddenInput)

    def clean(self):
        password1 = self.cleaned_data.get('new_password1')
        old = self.cleaned_data.get('old_password')
        username = self.cleaned_data.get('username')

        if len(password1) < 14:
            raise ValidationError(
                "The new password must be at least 14 characters long.")

        # At least one letter and one non-letter
        first_isalpha = password1[0].isalpha()
        if all(c.isalpha() == first_isalpha for c in password1):
            raise ValidationError(
                "The new password must contain at least one letter " \
                 "and at least one digit or punctuation character.")

        if username in password1:
            raise ValidationError("Password main not contain your username.")

        if password1 == old:
            raise ValidationError("Must be different than your old password.")

        if all(c.islower() for c in re.sub(r'\W+', '', password1)):
            raise ValidationError('Must contain at least 1 Upper case letter')
 