# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('konular', '0002_auto_20161115_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='konular',
            name='Css',
        ),
        migrations.RemoveField(
            model_name='konular',
            name='Js',
        ),
        migrations.AlterField(
            model_name='konular',
            name='Icerik',
            field=tinymce.models.HTMLField(verbose_name='\u0130\xe7erik', blank=True),
        ),
    ]
