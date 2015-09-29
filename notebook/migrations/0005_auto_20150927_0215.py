# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0004_auto_20150925_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='contact',
            field=models.ForeignKey(related_name='phones', to='notebook.Contact'),
        ),
    ]
