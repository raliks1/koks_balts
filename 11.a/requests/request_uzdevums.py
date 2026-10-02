import statistics
from statistics import mean, median

# 1. Datu iegūšana - API pieprasījums
x = requests.get("https://randomuser.me/api/?results=10").json()

# 2. Datu apstrāde - vecumu saraksts un cilvēku informācija
vecumi = []
user_info = []

print("Nejaušu cilvēku dati:")
print("-" * 50)

for ieraksts in x["results"]:
    vards = f'{ieraksts["name"]["first"]} {ieraksts["name"]["last"]}'
    vecums = ieraksts["dob"]["age"]
    vecumi.append(vecums)
    user_info.append((vards, vecums))
    print(f'{vards}: {vecums} gadi')

print("-" * 50)

# 3. Analīze - vidējais vecums un mediāna
videjais_vecums = mean(vecumi)
medianas_vecums = median(vecumi)

print(f"\nVidējais vecums: {videjais_vecums:.2f}")
print(f"Mediānais vecums: {medianas_vecums}")

# 4. Saglabāšana failā petijums.txt
with open('petijums.txt', 'w', encoding='utf-8') as f:
    f.write("NEJAUŠU CILVĒKU GRUPU PĒTĪJUMS\n")
    f.write("=" * 50 + "\n\n")
    f.write("Cilvēku dati:\n")
    f.write("-" * 50 + "\n")
    
    for vards, vecums in user_info:
        f.write(f"{vards}: {vecums} gadi\n")
    
    f.write("-" * 50 + "\n\n")
    f.write("STATISTIKA:\n")
    f.write(f"Vidējais vecums: {videjais_vecums:.2f}\n")
    f.write(f"Mediānais vecums: {medianas_vecums}\n")

print("\nRezultāti saglabāti failā 'petijums.txt'")
