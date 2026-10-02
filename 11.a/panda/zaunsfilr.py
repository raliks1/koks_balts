import os
os.system('cls')
print("\n")

import pandas
from datetime import datetime
import ctypes 

df = pandas.read_csv("saraksts.csv", sep=';', dtype=str)
# print(df.to_string)

input_data = input("Ievadiet datumu(DD.MM):")

df["Dzimšanas datums"] = df["Dzimšanas datums"].str[:5]

bd_skoleni = df[df["Dzimšanas datums"] == input_data]

print(bd_skoleni)

if not bd_skoleni.empty:
    teksts = "Sveicam dzimšanas dienā!!!\n\n"
    for _, row in bd_skoleni.iterrows():
        teksts += f"{row['Vārds'].upper()}\n{row['Klase'].upper()}\n{row['Deklarētā adrese'].upper()}\n\n"
else:
    teksts = "Šodien nav nevienam dz.diena!!!!"

ctypes.windll.user32.MessageBoxW(0,teksts.strip(), "svinam", 1)

