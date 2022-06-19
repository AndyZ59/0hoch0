# 0hoch0.py
#
# finde Zwischenextrem (Grenzwert bei 0,34) für Null hoch Null
#
# 01 31.aug.2021 az	    im Handy
# 02 01.Sep.2021 az V 	loop für autom Finden
# 03 03.Sep.2021 az     loop für autom Finden
#                       Python 3.9.7 64Bit (Win store)

# open:
# doppelte Genauigkeit


def schleife(start=0.5, loop=3):
    for i in range(loop):
        print("       start: ", start)
        print(start ** start)
        start = start * 0.99


def entscheidung(loop=3):
    zahl = 0.35            # Startwert
    delta = 0.1                 # = 10%
    wert1 = zahl ** zahl
    wert2 = 0.6                 # erster Vergleichswert
    
    i = 1
    while (i != loop):          # max Abbruchkriterium
        print("\n           loop: ", str(i).rjust(4), "  ", zahl)
        print(" w1 ", wert1)

        #vzPos = True

        if i != 1:              # nicht berechnen beim 1. Durchlauf
            wert2 = zahl ** zahl
        print(" w2 ", wert2)

        if wert2 < wert1:       # neuer Wert ist kleiner
            print("wird kleiner")
            zahl *= (1 + delta)
        else:                   # neuer Wert ist größer
            print("wird grösser")
            delta /= -2             # halbe Schrittweite mit anderem Vorzeichen
            zahl *= (1 + delta)

        if wert2 == wert1:      # fertig
            break

        wert1 = wert2
        i += 1


# ....... main ...........
# schleife(wert1,30)
entscheidung(100)

n=float(1/7)
print("\n%.50f"%n) # 4.000000
