while True:
    age = int(input("Hány éves vagy?"))

    kerdes = input("Mit iszol? (Sört vagy kólát?)")

    if kerdes != 'sört' and kerdes != 'Kólat':
        print("Csak sört és kólát tudunk adni.")
        exit()

    if age < 18 and kerdes == 'sört':
        print("Sajnos nem adhatok")
    elif age >= 60 and kerdes == 'kólát':
        print("Megemelheti a vérnyomását!")
    else:
        print(f'Parancsoljon, itt a {kerdes}')
