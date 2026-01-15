import os 
os.system('cls')
print("\n")

from num2words import num2words
import statistics

reitingi = [8.5, 9.1, 7.5, 9.1, 8.8, 8.5, 7.9]

print(f"oriģinālie reitingi {reitingi}")

print("vidējā vērtība ir:", statistics.median(reitingi))

reitingu_vid = statistics.mean(reitingi)
print(f"vidējā vērtība (mean) ir {reitingu_vid}")

print("lielākais reitings ir", num2words(max(reitingi), lang='lv'))

reitingu_īsākais = min(reitingi)
print(f"mazākais reitings ir {reitingu_īsākais}")

reitingu_moda = statistics.mode(reitingi)
print(f"biežākais reitings ir {reitingu_moda}")