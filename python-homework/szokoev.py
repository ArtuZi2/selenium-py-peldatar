#Nem sikerült még megoldanom, de nem adom még fel.

def szokoev_kiiratas(evszam):
    return evszam
evszam = int(input("Írj be egy évszámot!"))


# evszam = int(input("Írj be egy évszámot!"))
if (evszam % 4) == 0 and (evszam % 400) == 0:
    print("Szökőév")
if (evszam % 2) == 0 and (evszam % 3) == 0 and (evszam % 4) != 0 and (evszam % 400) != 0:
    print("Nem szökőév")



