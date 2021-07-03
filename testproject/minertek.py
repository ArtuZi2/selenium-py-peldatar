three_numbers = input("Írj be három számot vesszővel elválasztva!")
three_numbers_list = three_numbers.split(",")

ertek = int(three_numbers_list[0])
for x in range(len(three_numbers_list)):
    if int(three_numbers_list[x]) < ertek:
        ertek = int(three_numbers_list[x])
print("minimum érték:", ertek)

l = []
for i in range(3):
    l.append(int(input("Írj be egy számot!")))
print(min(l))
