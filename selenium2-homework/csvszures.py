import csv

with open("table_in.csv", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    for row in csvreader:
        print(f'Name: {row[0]} Email: {row[1]}')