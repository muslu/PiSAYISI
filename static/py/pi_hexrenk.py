# -*- coding: utf-8 -*-


PiDosyasi = "pi_100000.txt"

Okunanlar = None

KacBasamak = 3000

with open(PiDosyasi, 'r') as file :
  Okunanlar = file.read()[0:KacBasamak].strip()


tablo = """
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
.tg td{padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-yw4l{vertical-align:top}
@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style>
<div class="tg-wrap"><table class="tg">
"""


Sira = 0
tabloTR = 0

with open('pi_hextablo.txt', 'w') as file:


    tablo += "<tr>"
    
    for k in Okunanlar:
        
        Sira += 1

        if Sira % 6 == 0:
            tablo += "<th class='tg-yw4l' style='background-color:#"+Okunanlar[Sira-6:Sira]+";'>"+Okunanlar[Sira-6:Sira]+"</th>"

        if Sira % 60 == 0:
            tablo += "</tr><tr>"

            
    tablo += "</table></div>"
    
    file.write("{}\n".format(str(tablo)))

#print tablo
