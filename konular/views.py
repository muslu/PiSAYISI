# -*- coding: utf-8 -*-
import os

from django.shortcuts import render

from konular.models import Kategoriler, AltKategoriler, Konular

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def pibasamak(kac):
    PiDosyasi = BASE_DIR + "/static/pi_100000.txt"

    Okunanlar = None

    with open(PiDosyasi, 'r') as file:
        Okunanlar = file.read()

    Sira = 0

    datalar = '['

    rakamlar = Okunanlar[0:int(kac)].strip()

    for k in rakamlar:
        Sira += 1
        datalar += '{ x: ' + str(Sira) + ', y: ' + str(k) + ' },'

    datalar = datalar[:-1] + ']'

    return str(datalar) + "++" + str(rakamlar)


def canvasjs(request):
    tur = request.GET.get('tur', '0')
    basamak = request.GET.get('basamak', '0')

    datalar_rakamlar = pibasamak(basamak)
    datapoint = datalar_rakamlar.split("++")[0]
    rakamlar = datalar_rakamlar.split("++")[1]

    KacTaneVar = "Kaç tane var: <br/>"
    for l in range(0, 10):
        KacTaneVar += str(l) + " : " + str(rakamlar.count(str(l))) + "<br/>"

    return render(request, 'canvasjs.html', {'tur': tur, 'basamak': basamak, 'datapoint': datapoint, 'rakamlar': rakamlar, 'KacTaneVar': KacTaneVar})


def paperjs(request):
    return render(request, 'paperjs.html', {})


def anasayfa(request):
    kategoriler = Kategoriler.objects.order_by('-id')
    return render(request, 'index.html', {'kategoriler': kategoriler})


def tum_konular(request):
    tumkonular = Konular.objects.order_by('-id')
    return render(request, 'tumkonular.html', {'tumkonular': tumkonular})


def kategori_detay(request, link):
    kategori = Kategoriler.objects.get(Link=link)
    kategori_detay = AltKategoriler.objects.filter(Kategorisi__Link=link).order_by('-id')
    return render(request, 'kategori_detay.html', {'kategori_detay': kategori_detay, 'kategori': kategori})


def konular(request, kat_link, altkat_link):
    altkategori = AltKategoriler.objects.get(Link=altkat_link)
    konular = Konular.objects.filter(AltKategorisi__Link=altkat_link, AltKategorisi__Kategorisi__Link=kat_link).order_by('-id')
    return render(request, 'konular.html', {'konular': konular, 'altkategori': altkategori})


def konu_detay(request, kat_link, altkat_link, link):
    if "canvasjs" in link:
        return canvasjs(request)

    if "paperjs" in link:
        return paperjs(request)

    konu_detay = Konular.objects.get(AltKategorisi__Link=altkat_link, AltKategorisi__Kategorisi__Link=kat_link, Link=link)
    return render(request, 'konu_detay.html', {'konu_detay': konu_detay})
