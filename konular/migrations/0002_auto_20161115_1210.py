# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('konular', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='konular',
            name='Css',
            field=models.TextField(default=datetime.datetime(2016, 11, 15, 12, 10, 13, 460667), help_text=b'css kodlar\xc4\xb1', verbose_name='Css'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='konular',
            name='Js',
            field=models.TextField(default=datetime.datetime(2016, 11, 15, 12, 10, 22, 387399), help_text=b'javascript kodlar\xc4\xb1', verbose_name='JS'),
            preserve_default=False,
        ),
    ]
