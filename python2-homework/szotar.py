lista = [11, 45, 8, 11, 23, 45, 23, 45, 89]
szótár = {}
for elem in lista:
    szótár[elem] = szótár.get(elem, 0) + 1
print(szótár)

[19:10] Tamas Jozsa
# 1) Adott számokat tartalmazó lista.
# Pl. [11, 45, 8, 11, 23, 45, 23, 45, 89]
#
# Írj egy olyan Python programot ami egy asszociatív tömbben eltárolja a lista elemeinek előfordulási számát.
#
# A fenti példára a kimenet: {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
