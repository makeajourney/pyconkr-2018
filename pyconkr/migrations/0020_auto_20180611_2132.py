# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyconkr', '0019_auto_20170712_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'ordering': ['deposit_time', 'id']},
        ),
        migrations.AddField(
            model_name='sponsor',
            name='deposit_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
