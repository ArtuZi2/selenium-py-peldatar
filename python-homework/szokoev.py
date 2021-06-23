#Nem sikerült még megoldanom, de nem adom még fel.

def szokoev_kiiratas(evszam):
    return evszam
evszam = int(input("Írj be egy évszámot!"))


# evszam = int(input("Írj be egy évszámot!"))
if (evszam % 4) == 0:
    print("Szökőév")
elif (evszam % 100) == 0:
        print("Nem szökőév")
elif (evszam % 400) == 0:
    print("Szökőév")
else:
    print("Nem szökőév")



