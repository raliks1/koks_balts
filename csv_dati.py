import os
os.system('cls')
print("\n")

import csv

with open("saraksts.csv", "r") as file:
    reader = csv.DictReader(file)
    viss_saraksts = {}
    for row in reader:
        rinda = row["saprotam?k? valoda"]
        if rinda in viss_saraksts:
            viss_saraksts[rinda] += 1
        else:
            viss_saraksts[rinda] = 1
for rinda in sorted(viss_saraksts, key=viss_saraksts.get, reverse=True):
    print(f"{rinda}: {viss_saraksts[rinda]}")


