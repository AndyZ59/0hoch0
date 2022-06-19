# 0hoch0.py
#
# Problem siehe Bild
#
# Berechnung wegen Widerspruch aus:
#   a ^ 0 = 1
#     und
#   0 ^ n = 0
# 
#
# finde Zwischenextrem (Grenzwert bei 0,34) für Null hoch Null
#   mittels Iteration mit doppelter Genauigkeit
# Ausgabe mit Schleifennummer
#   Abbruch bei max-Schleifen ODER gefunden
#
# Ver   Datum   wer     Änderung
# - - - - - - - - - - - - - - - - - - - - - - -
# 01 31.aug.2021 az	    im Handy
# 02 01.Sep.2021 az V 	loop für autom Finden
# 03 03.Sep.2021 az     loop für autom Finden
#                       Python 3.9.7 64Bit (Win store)
# 04 08.Sep.2021 az     doppelte Genauigkeit
#                       siehe Erklärung
# 05 18.Jun.2022 az     Erläuterungen ergänzt für upload ins github
#                       Python 3.9.13 64Bit (Win store)


# open:



'''
#----------- Erklärung ---------------

doppelte Genauigkeit

from https://zetcode.com/python/decimal/
    #!/usr/bin/python

    from decimal import Decimal

    x = 1 / 7
    print(type(x))
    print(x)                # 18 digits

    print("-----------------------")

    y = Decimal(1) / Decimal(7)
    print(type(y))
    print(y)                # 28 digits

'''

from decimal import Decimal

def schleife(start=0.5, loop=3):
    for i in range(loop):
        print("       start: ", start)
        print(start ** start)
        start = start * 0.99


def entscheidung(loop=3):
    zahl = 0.5            # Startwert
    delta = 0.1                 # = 10%
    wert1 = zahl ** zahl
    wert2 = 0.7                 # erster Vergleichswert
    
    i = 1
    while (i != loop):          # max Abbruchkriterium
        print("\n           loop: ", str(i).rjust(4), "  ", zahl)
        print(" w1 ", wert1)

        #vzPos = True

        if i != 1:              # nicht berechnen beim 1. Durchlauf
            wert2 = Decimal(zahl) ** Decimal(zahl)
        print(" w2 ", wert2)

        if wert2 < wert1:       # neuer Wert ist kleiner
            print("wird kleiner")
        elif wert2 > wert1:                   # neuer Wert ist größer
            print("wird grösser")
            delta /= -2             # halbe Schrittweite mit anderem Vorzeichen
        else:                   # neuer Wert ist größer
            print("--------- ist gleich -------\n\n")
            break
        zahl = Decimal(zahl) * Decimal((1 + delta))

        wert1 = Decimal(wert2)
        i += 1
    

# ....... main ...........
# schleife(wert1,30)
entscheidung(200)

print("-----------------------")
print("-----------------------")
# Darstellung der doppelten Genauigkeit

x = 1 / 7
print(type(x))
print(x)                # 18 digits

print("-----------------------")

y = Decimal(1) / Decimal(7)
print(type(y))
print(y)                # 28 digits
print("%.100f"%y)       # 100 digits
print()
