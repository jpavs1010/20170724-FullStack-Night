# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-18 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DictEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('definition', models.CharField(max_length=500)),
            ],
        ),
    ]
