# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180106_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, default='No Image', upload_to=''),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
