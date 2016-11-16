from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from konular.views import *

urlpatterns = [

    url(r'^$', anasayfa),

    # url(r'^amp/python/istanbul/$', amp_anasayfa),
    # url(r'^amp/([\w\-]+)/kategorisi/$', amp_kategori_detay),
    # url(r'^amp/([\w\-]+)/([\w\-]+)/kategorisi/$', amp_konular),
    # url(r'^amp/([\w\-]+)/([\w\-]+)/([\w\-]+)/konusu/$', amp_konu_detay),

    url(r'^tum-konular/$', tum_konular),
    url(r'^([\w\-]+)/kategorisi/$', kategori_detay),
    url(r'^([\w\-]+)/([\w\-]+)/konusu/$', konular),
    url(r'^([\w\-]+)/([\w\-]+)/([\w\-]+)/konu-detayi/$', konu_detay),


    # url(r'^$', TemplateView.as_view(template_name="index.html")),

    url(r'^hakkimizda/$', TemplateView.as_view(template_name="hakkimizda.html")),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
