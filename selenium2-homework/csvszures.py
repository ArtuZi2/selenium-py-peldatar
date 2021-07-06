import csv

#row = table_in_csv[table_in_csv.find('Email'):table_in_csv.find('name')]
with open("table_in_csv", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    for row in csvreader:
        print(f'Name: {row[0]} Email: {row[1]}')