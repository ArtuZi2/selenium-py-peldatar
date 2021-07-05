#Jelenlegi évszám - age = születési év, 100-age = év100hoz, jelenlegi evszam+év100hoz
from datetime import date
import datetime

name = input("Hogy hívnak?")
age = int(input("Hány éves vagy?"))

year = datetime.datetime.today().year

print(name,"ebben az évben leszel 100 éves:", year + 100 - age)