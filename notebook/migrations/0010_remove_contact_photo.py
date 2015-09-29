# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0009_auto_20150929_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='photo',
        ),
    ]
