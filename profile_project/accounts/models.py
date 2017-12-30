import datetime
from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.EmailField(max_length=75)
    date_of_birth = models.DateField(default=datetime.date.today)
    bio = models.TextField(max_length=512)
    avatar = models.ImageField(default='No Image')
