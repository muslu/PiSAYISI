# -*- coding: utf-8 -*-




PiDosyasi = "pi_100000.txt"

Okunanlar = None

with open(PiDosyasi, 'r') as file :
  Okunanlar = file.read()

  
with open('pi_toplamali.txt', 'w') as file:
    Toplam = 0
    Sira = 0
    for k in Okunanlar:
	Sira += 1
	if Sira % 2 != 0:
	    print str(Toplam) + " + " + str(k)+ " = " + str(Toplam + int(k))
	    
	    if len(str(Toplam)) in (1,2,3):
		file.write("{}\t\t\t+\t\t{}\t=\t{}\n".format(str(Toplam), str(k), str(Toplam + int(k))))
	    else:
		file.write("{}\t\t+\t\t{}\t=\t{}\n".format(str(Toplam), str(k), str(Toplam + int(k))))
	    Toplam = Toplam + int(k)
	else:
	    print str(Toplam) + " - " + str(k)+ " = " + str(Toplam - int(k))
	    
	    if len(str(Toplam)) in (1,2,3):
		file.write("{}\t\t\t-\t\t{}\t=\t{}\n".format(str(Toplam), str(k), str(Toplam - int(k))))
	    else:
		file.write("{}\t\t-\t\t{}\t=\t{}\n".format(str(Toplam), str(k), str(Toplam - int(k))))
	    Toplam = Toplam - int(k)


