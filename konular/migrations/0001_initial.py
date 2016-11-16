# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AltKategoriler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Baslik', models.CharField(max_length=150, verbose_name='Ba\u015fl\u0131k')),
                ('Icerik', tinymce.models.HTMLField(verbose_name='\u0130\xe7erik')),
                ('Link', models.SlugField(max_length=250, verbose_name='Otomatik Link')),
            ],
            options={
                'verbose_name': 'Alt Kategori',
                'verbose_name_plural': '2 - Alt Kategoriler',
            },
        ),
        migrations.CreateModel(
            name='Kategoriler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Baslik', models.CharField(max_length=150, verbose_name='Ba\u015fl\u0131k')),
                ('Icerik', tinymce.models.HTMLField(verbose_name='\u0130\xe7erik')),
                ('Link', models.SlugField(max_length=250, verbose_name='Otomatik Link')),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': '1 - Kategoriler',
            },
        ),
        migrations.CreateModel(
            name='Konular',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Baslik', models.CharField(max_length=150, verbose_name='Ba\u015fl\u0131k')),
                ('Yazar', models.CharField(max_length=150, verbose_name='Yazar')),
                ('Icerik', tinymce.models.HTMLField(verbose_name='\u0130\xe7erik')),
                ('Link', models.SlugField(max_length=250, verbose_name='Otomatik Link')),
                ('IslemTarihi', models.DateTimeField(auto_now=True, verbose_name='\u0130\u015flem Tarihi')),
                ('AltKategorisi', models.ForeignKey(to='konular.AltKategoriler')),
            ],
            options={
                'verbose_name': 'Konu',
                'verbose_name_plural': '3 - Konular',
            },
        ),
        migrations.AddField(
            model_name='altkategoriler',
            name='Kategorisi',
            field=models.ForeignKey(to='konular.Kategoriler'),
        ),
    ]
