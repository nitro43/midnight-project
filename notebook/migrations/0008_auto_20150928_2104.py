# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0007_auto_20150928_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
