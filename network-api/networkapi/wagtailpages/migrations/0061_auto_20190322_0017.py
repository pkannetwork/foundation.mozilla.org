# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-22 00:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0060_auto_20190320_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarypage',
            name='banner',
            field=models.ForeignKey(blank=True, help_text="Choose an image that's bigger than 4032px x 1152px with aspect ratio 3.5:1", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_banner', to='wagtailimages.Image', verbose_name='Hero Image'),
        ),
    ]
