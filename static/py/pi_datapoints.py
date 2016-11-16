# -*- coding: utf-8 -*-

PiDosyasi = "pi_100000.txt"

Okunanlar = None

with open(PiDosyasi, 'r') as file :
    Okunanlar = file.read()


Sira = 0

datalar = 'dataPoints: ['


for k in Okunanlar.strip():
    Sira += 1
    datalar += '{ x: ' + str(Sira) + ', y: ' + str(k) + ' },'
    
datalar = datalar[:-1] + ']'

with open('pi_dataPoints.txt', 'w') as file:
    file.write(datalar)
	
	

