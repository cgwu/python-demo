# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-24 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jj2app', '0004_auto_20180324_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='remark',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]