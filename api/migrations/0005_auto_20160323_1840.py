# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160317_0206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drop',
            options={'ordering': ['-id']},
        ),
    ]
