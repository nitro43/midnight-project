# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('contact', models.ForeignKey(to='notebook.Contact')),
            ],
        ),
    ]
