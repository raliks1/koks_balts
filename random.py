import os 
os.system('cls')
print("\n")

import random

# krasas = ["sarkans", "zals", "zils"]
# krasasNr1 = random.choice(krasas)
# krasasNr2 = random.choice(krasas)

# print("izveletas krasas ir:", krasasNr1, "un", krasasNr2)
# import string
# iespejamas_rakstzimes = list(string.ascii_lowercase + string.digits)
# parole = ""

# for _ in range(9):
#     rakstzime = random.choice(iespejamas_rakstzimes)

#     parole += rakstzime

#     print("Ģenerētā parole ir:", parole)

# jautajumi = [
#     "Kas ir Python interpretators?",
#     "Paskaidro atšķirību starp LIST un TUPLE!",
#     "Kā importē moduli 'math'?",
#     "Kas ir cikls 'for'?",
#     "Miniet divus datu tipus Pythonam!"
# ]
# for i, jautajums in enumerate(jautajumi):
#     print(f"{i+1}, **{jautajums}**")
# najausais_indekss = random.randint(0, len(jautajumi) - 1)

# print("\nNejauši izvēlētais jautājums ir:")

# papildus_jautajums = jautajumi[najausais_indekss]

# print(f"pārsteiguma jautājums -> {papildus_jautājums}")
from num2words import num2words
import statistics

reitingi = [8.5, 9.1, 7.5, 9.1, 8.8, 8.5, 7.9]

print(f"oriģinālie reitingi {reitingi}")

reitingu_mediana = statistics.median(reitingi)
print(f"veidējā vērtība (mediāna) ir {reitingu_mediana}")

reitingu_vid = statistics.mean(reitingi)
print(f"vidējā vērtība (mean) ir {reitingu_vid}")

reitingu_lielakais = max(reitingi)
print(f"lielākais reitings ir {reitingu_lielakais}")

reitingu_īsākais = min(reitingi)
print(f"mazākais reitings ir {reitingu_īsākais}")

reitingu_moda = statistics.mode(reitingi)
print(f"biežākais reitings ir {reitingu_moda}")


# jaunie_reitingi = [reitingi * 10 for reitingi in reitingi]

# print(f"jaunie reitingi {jaunie_reitingi}")

# orig_mean = statistics.mean(jaunie_reitingi)
# simtiem_mean = statistics.mean(reitingi) 







