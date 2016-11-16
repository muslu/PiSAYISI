# -*- coding: utf-8 -*-

from django.contrib import admin
from konular.models import Konular, Kategoriler, AltKategoriler


class KategorilerAdmin(admin.ModelAdmin):
    list_display            =       [ 'Baslik',]
    actions_on_bottom       =       True
    actions_on_top          =       True
    list_per_page           =       100
    prepopulated_fields     =       {'Link': ('Baslik',) }

admin.site.register(Kategoriler, KategorilerAdmin)

class AltKategorilerAdmin(admin.ModelAdmin):
    list_display            =       [ 'Kategorisi', 'Baslik',]
    actions_on_bottom       =       True
    actions_on_top          =       True
    list_per_page           =       100
    prepopulated_fields     =       {'Link': ('Baslik',) }

admin.site.register(AltKategoriler, AltKategorilerAdmin)


class KonularAdmin(admin.ModelAdmin):
    list_display            =       [ 'AltKategorisi', 'Yazar', 'Baslik', 'IslemTarihi']
    ordering                =       ['-IslemTarihi', ]
    actions_on_bottom       =       True
    actions_on_top          =       True
    list_per_page           =       100
    date_hierarchy          =       'IslemTarihi'
    prepopulated_fields     =       {'Link': ('Baslik',) }

admin.site.register(Konular, KonularAdmin)

