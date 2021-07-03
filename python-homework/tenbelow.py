n = 0
szamok = []
while True:
    n = int(input("Írj be egy számot!"))
    if n >= 10:
        break
    else:
        szamok.append(n)
print("A 10-nél kisebb megadott számok összege: ", sum(szamok))


