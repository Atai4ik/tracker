# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailprofile',
            options={'verbose_name': '\u041f\u0440\u043e\u0444\u0438\u043b\u044c', 'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0438\u043b\u0438'},
        ),
        migrations.AddField(
            model_name='detailprofile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=20),
        ),
    ]
