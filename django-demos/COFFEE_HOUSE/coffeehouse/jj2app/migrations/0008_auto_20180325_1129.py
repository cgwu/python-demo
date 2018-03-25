# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('jj2app', '0007_auto_20180325_0730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'ordering': ['-state']},
        ),
        migrations.AlterModelManagers(
            name='store',
            managers=[
                ('mgr', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddIndex(
            model_name='store',
            index=models.Index(fields=['city', 'state'], name='jj2app_stor_city_f4f68c_idx'),
        ),
        migrations.AddIndex(
            model_name='store',
            index=models.Index(fields=['city'], name='jj2app_stor_city_2ebc7e_idx'),
        ),
    ]
