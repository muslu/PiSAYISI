# -*- coding: utf-8 -*-


PiDosyasi = "pi_100000.txt"

Okunanlar = None

KacBasamak = 10000

with open(PiDosyasi, 'r') as file :
  Okunanlar = file.read()[0:KacBasamak].strip()


for l in range(0,10):
    print str(l) + " : " + str(Okunanlar.count(str(l)))

