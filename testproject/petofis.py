with open("petofi.txt", 'r', encoding="utf-8") as petofi:
    with open("res.csv", 'w', encoding="utf-8") as res:
        words = petofi.read().replace("\n", " ").replace(" ", "").split(",")
        for word in words[::2]:
            res.write(f"{words.index(word)}, {word.lower()}\n")


with open("petofi.txt", 'r', encoding="utf-8") as petofi:
    with open("res.csv", 'w', encoding="utf-8") as res:
        words = petofi.read().replace("\n", " ").replace(" ", "").split(",")
        for i, word in list(enumerate(words))[::2]:
            res.write(f"{i+1}, {word}\n")

with open("petofi.txt", 'r', encoding="utf-8") as petofi:
    with open("res.csv", 'w', encoding="utf-8") as res:
        words = petofi.read().replace("\n", " ").replace(",", "").split(" ")
        for i, word in list(enumerate(words))[1::2]:
            res.write(f"{i+1}, {word}\n")