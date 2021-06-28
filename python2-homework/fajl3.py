with open("adat.txt", "r") as f:
    result = f.readlines()
    print(result)
with open("adat2.txt", "a") as k:
    k.write("Egyszer volt, hol nem volt, vol egyszer egy ember")
    result2 = k.readlines()
    print(k)