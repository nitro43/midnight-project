# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0008_auto_20150928_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='photo',
            field=models.ImageField(upload_to='static/images', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='adress',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
