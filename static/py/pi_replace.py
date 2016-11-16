# -*- coding: utf-8 -*-


geometre = {
        1: 'Alef',
        2: 'Bet',
        3: 'Gimel',
        4: 'Dalet',
        5: 'He',
        6: 'Vav',
        7: 'Zayin',
        8: 'Het',
        9: 'Tet',
        10: 'Yod',
        20: 'Kaph',
        30: 'Lamed',
        40: 'Mem',
        50: 'Nun',
        60: 'Samek',
        70: 'Ayin',
        80: 'Pe',
        90: 'Tsadik',
        100: 'Kuf',
        200: 'Reş',
        300: 'Şin',
        400: 'Tav',
        500: 'Kaph',
        600: 'Mem',
        700: 'Nun',
        800: 'Pe',
        900: 'Tsadik',
        }

geometre_char = {
        1: 'א',
        2: 'ב',
        3: 'ג',
        4: 'ד',
        5: 'ה',
        6: 'ו',
        7: 'ז',
        8: 'ח',
        9: 'ט',
        10: 'י',
        20: 'ך',
        30: 'ל',
        40: 'ם',
        50: 'ן',
        60: 'ס',
        70: 'ע',
        80: 'ף',
        90: 'ץ',
        100: 'ק',
        200: 'ר',
        300: 'ש',
        400: 'ת',
        500: 'כ',
        600: 'מ',
        700: 'נ',
        800: 'פ',
        900: 'צ',
        }

        

PiDosyasi = "pi_100000.txt"

Okunanlar = None

KacBasamak = 10000

with open(PiDosyasi, 'r') as file :
  Okunanlar = file.read()[0:KacBasamak].strip()


with open('pi_geometre.txt', 'w') as file:
    
    for key in sorted(geometre, reverse=True):
        Okunanlar = Okunanlar.replace(str(key), str(geometre[key][0:1]))
        
    file.write("{}\n".format(str(Okunanlar)))

print Okunanlar


