import csv

print("program berjalan")

with open("data_film.csv", "r") as file:
    data = csv.reader(file)

    for baris in data:
        print(baris)
    