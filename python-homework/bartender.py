age = int(input("Hány éves vagy?"))
kerdes = str(input("Mit iszol?"))

if age < 18 and kerdes == 'Sört' :
    print("Sajnos nem adhatok")
else:
    print("Parancsoljon, a söre")

if age >= 60 and kerdes == 'kólát':
    print("Megemelheti a vérnyomását!")

if kerdes != 'sört' and kerdes != 'kólát':
    print("Csak sört és kólát tudunk adni")


# else:
    #print("Parancsoljon, a söre!")
    #print("Parancsoljon, a kólája!")

# if age >= 18 and age > 60 and kerdes == 'sört':
    #print("Parancsoljon, a söre!")
# if age <= 18 and age < 60 or kerdes == 'kólát':
    #print("Parancsoljon, a kólája!")
