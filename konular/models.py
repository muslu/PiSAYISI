# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField


class Kategoriler(models.Model):
    Baslik          =       models.CharField( u'Başlık', max_length = 150 )
    Icerik          =       HTMLField( u'İçerik', )
    Link            =       models.SlugField( u'Otomatik Link', max_length = 250 )

    def __unicode__(self):
        return self.Baslik

    class Admin:
        js = ('js/tiny_mce/tiny_mce.js', 'js/tiny_mce/textareas.js')

    class Meta:
        verbose_name_plural             =       u"1 - Kategoriler"
        verbose_name                    =       u"Kategori"


class AltKategoriler(models.Model):
    Kategorisi      =       models.ForeignKey(Kategoriler)
    Baslik          =       models.CharField( u'Başlık', max_length = 150 )
    Icerik          =       HTMLField( u'İçerik', )
    Link            =       models.SlugField( u'Otomatik Link', max_length = 250 )

    def __unicode__(self):
        return "%s - %s" % (self.Kategorisi.Baslik, self.Baslik)

    class Admin:
        js = ('js/tiny_mce/tiny_mce.js', 'js/tiny_mce/textareas.js')

    class Meta:
        verbose_name_plural             =       u"2 - Alt Kategoriler"
        verbose_name                    =       u"Alt Kategori"



class Konular(models.Model):
    AltKategorisi        =       models.ForeignKey(AltKategoriler)
    Baslik              =       models.CharField( u'Başlık', max_length = 150 )
    Yazar               =       models.CharField( u'Yazar', max_length = 150 )
    # Js                  =       models.TextField( u'JS', help_text="javascript kodları")
    # Css                 =       models.TextField( u'Css', help_text="css kodları")
    Icerik              =       HTMLField( u'İçerik', blank = True)
    Link                =       models.SlugField( u'Otomatik Link', max_length = 250 )
    IslemTarihi         =       models.DateTimeField ( u"İşlem Tarihi", auto_now = True)

    class Admin:
        js = ('js/tiny_mce/tiny_mce.js', 'js/tiny_mce/textareas.js')

    def __unicode__(self):
        return "%s - %s - %s" % (self.AltKategorisi.Kategorisi.Baslik, self.AltKategorisi.Baslik, self.Baslik)

    class Meta:
        verbose_name_plural             =       u"3 - Konular"
        verbose_name                    =       u"Konu"

