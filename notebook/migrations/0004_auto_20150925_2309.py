# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0003_auto_20150925_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phones',
        ),
        migrations.AddField(
            model_name='phone',
            name='contact',
            field=models.ForeignKey(to='notebook.Contact', default=1),
            preserve_default=False,
        ),
    ]
