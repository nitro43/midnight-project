# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0002_auto_20150922_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='phones',
            field=models.ForeignKey(default=2, to='notebook.Phone'),
            preserve_default=False,
        ),
    ]
