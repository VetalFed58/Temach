# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-12-07 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
