# -*- coding: utf-8 -*-


PiDosyasi = "pi_100000.txt"

Okunanlar = None

KacBasamak = 10000

with open(PiDosyasi, 'r') as file :
  Okunanlar = file.read()[0:KacBasamak].strip()


Sira = 0

tablo = """
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
.tg td{padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-yw4l{vertical-align:top}
@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style>
<div class="tg-wrap"><table class="tg">
"""


with open('pi_latlong.txt', 'w') as file:

       
    tablo += "<tr>"
    
    for k in Okunanlar:
        
        Sira += 1

        if Sira % 20 == 0:
            
            LatLong = Okunanlar[Sira-10:Sira][0:2] + "." + Okunanlar[Sira-10:Sira][2:10]
            LatLong2 = Okunanlar[Sira-20:Sira][0:2] + "." + Okunanlar[Sira-20:Sira][2:10]
            
            tablo += "<td><a href='https://www.google.com.tr/maps/@" +LatLong2 + "," + LatLong+ ",10z' target='_blank'>"+LatLong2 + " , " + LatLong+"</a></td>"

            #print LatLong2 + "," + LatLong

            tablo += "</tr><tr>"

    tablo += "</table></div>"
    
    file.write("{}\n".format(str(tablo)))
    

#print tablo
