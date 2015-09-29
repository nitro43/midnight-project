# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0006_auto_20150928_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(max_length=30),
        ),
    ]
