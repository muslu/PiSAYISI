# -*- coding: utf-8 -*-


PiDosyasi = "pi_100.txt"

Okunanlar = None

with open(PiDosyasi, 'r') as file :
  Okunanlar = file.read()


for l in range(0,9):
    print str(l) + ":" + str(Okunanlar.count(str(l)))

