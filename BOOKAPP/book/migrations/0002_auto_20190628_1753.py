# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-28 09:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
        migrations.AlterModelOptions(
            name='heroinfo',
            options={'verbose_name': '英雄', 'verbose_name_plural': '英雄'},
        ),
        migrations.AlterModelTable(
            name='bookinfo',
            table='tb_book',
        ),
        migrations.AlterModelTable(
            name='heroinfo',
            table='tb_hero',
        ),
    ]
