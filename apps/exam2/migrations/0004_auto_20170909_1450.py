# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam2', '0003_quote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='desc',
            new_name='message',
        ),
        migrations.AddField(
            model_name='quote',
            name='quoted_by',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]