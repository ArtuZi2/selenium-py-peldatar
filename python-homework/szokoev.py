#Nem sikerült még megoldanom, de nem adom még fel.

def szokoev_kiiratas(evszam):
    return evszam
evszam = int(input("Írj be egy évszámot!"))


# evszam = int(input("Írj be egy évszámot!"))
if (evszam % 4) == 0 and (evszam % 400) == 0:
    print("Szökőév")
if (evszam % 2) == 0 and (evszam % 3) == 0 and (evszam % 4) != 0 and (evszam % 400) != 0:
    print("Nem szökőév")


    def is_szokoev(ev):
        if ev % 4 == 0:
            if ev % 100 == 0:
                if ev % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


    def main_szoko():
        print(2005, is_szokoev(2005))
        print(2000, is_szokoev(2000))
        print(1980, is_szokoev(1980))
        print(1900, is_szokoev(1900))


    main_szoko()



