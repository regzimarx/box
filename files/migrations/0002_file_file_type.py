# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-03 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.CharField(default='.zip', max_length=16),
            preserve_default=False,
        ),
    ]
