#Nem sikerült még megoldanom, de ezt sem adom fel.

def checkalpha(index):
    if chr(index).isalpha():
        return chr(index)
    else:
        return ""


def check_last_column(index):
    if chr(index).isalpha():
        return index
    else:
        return ""


counter = 97
for i in range(10):
    print(chr(counter), counter,
          chr(counter + 11), counter + 11,
          checkalpha(counter + 21), check_last_column(counter + 21))
    counter += 1

for i in range(97, 122, 3):
    szam = i
    print(chr(szam), i, "\tb", i + 1, "\tc", i + 2)
