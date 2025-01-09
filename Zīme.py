import os
os.system('cls') #attira terminala logu pasa sakuma
print("\n") # ieliek tuksu rindinu pirms izdrukas

ievade = input("ievadiet transportliszekla numura zimes atdalot tās ar komatiem: ")

numuri = ievade.split(',')

for numurs in numuri:
    numurs = numurs.strip()
    if len(numurs) < 4 or '-' not in numurs:
        print(f"{numurs}:Numura zīme nav derīga.")
        continue

    burti, cipari, = numurs.split('-')

    if len(burti) != 2 or not all(burts.isalpha() and burts in "ABCDFGHIJKLMNOPRSTUVZ" for burts in burti.upper()):
        print(f"{numurs}: Numura zīme nav derīga.")
        continue

    if not cipari.isdigit() or not (1 <= int(cipari) <= 9999):
        print(f"{numurs}: Numura zīme nav derīga.")
        continue

    print(f"{numurs}: Numura zīme ir derīga.")
        