# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20171011_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='date_entered',
            field=models.DateTimeField(),
        ),
    ]
