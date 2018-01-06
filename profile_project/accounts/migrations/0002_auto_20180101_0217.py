# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(primary_key=True, default='', serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
