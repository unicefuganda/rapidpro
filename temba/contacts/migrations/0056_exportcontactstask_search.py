# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0055_auto_20170228_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='exportcontactstask',
            name='search',
            field=models.TextField(blank=True, help_text='The search query', null=True),
        ),
    ]
