# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 16:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_projectpost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectPost',
            new_name='Post',
        ),
    ]
