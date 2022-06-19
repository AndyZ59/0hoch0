# 0hoch0.py
#
# finde Zwischenextrem (Grenzwert bei 0,34) für Null hoch Null
#
# 01 31.aug.2021 az		im Handy
# 02 01.Sep.2021 az 	V 	loop für autom Finden

# open:
# doppelte Genauigkeit


wert1 = 0.8
fak = 0.9


def schleife(start=0.5, loop=3):
    for i in range(loop):
        print("       start: ", start)
        print(start ** start)
        start = start * 0.99


def entscheidung(loop=3):
    #zahl = 0.3679
    zahl = 0.36029
    wert1 = zahl ** zahl
    zahl *= 0.999
    vz = "kl"              # Vorzeichen 0: w2 < w1
    for i in range(1, loop+1):
        print("\n           loop: ", str(i).rjust(4), "  ", zahl)
        wert2 = zahl ** zahl
        print("w1 ", wert1)
        print("w2 ", wert2)
        if wert2 <= wert1:       # vz = "kl" \
            print("wird kleiner")
            if vz == "gr":         # missed
                zahl *= 0.9999999
                vz = "kl"
            else:
                pass
                zahl *= 0.999
        else:                   # vz = 1 /
            print("wird grösser")
            if vz == "kl":
                zahl *= 1.0000001
            else:
                #pass           # missed
                zahl **= 0.999
                #zahl *= 1.1
                vz = "gr"
        
        wert1 = wert2
            

# ....... main ...........
# schleife(wert1,30)
entscheidung(50)
