import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    first_name = models.CharField(max_length=75, blank=True)
    last_name = models.CharField(max_length=75, blank=True)
    email = models.EmailField(max_length=75, blank=True)
    date_of_birth = models.DateField(default=datetime.date.today, blank=True)
    bio = models.TextField(max_length=512, blank=True)
    avatar = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        if self.email:
            return self.email
        return self.first_name
