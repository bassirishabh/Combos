# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_auto_20170901_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_form',
            name='file',
            field=models.CharField(max_length=10),
        ),
    ]
