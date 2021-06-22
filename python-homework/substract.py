orszaguton = int(input("Mennyit fogyaszt országúton az autód?"))
varosban = int(input("Mennyit fogyaszt városban az autód?"))

orszaguton_km = int(input("Hány kilométert utaztál országúton?"))
varosban_km = int(input("Hány kilométert utaztál városban?"))

fogyasztas_oda = (orszaguton_km / 100 * orszaguton) + (varosban_km / 100 * varosban)
print(fogyasztas_oda)

fogyasztas_oda_vissza = ((orszaguton_km / 100 * orszaguton) + (varosban_km / 100 * varosban)) * 2
print(fogyasztas_oda_vissza)

teljes_ut_ara = fogyasztas_oda_vissza * 350
print(teljes_ut_ara)