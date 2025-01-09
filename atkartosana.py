import os
os.system('cls')
print("\n")

#1.uzdevums
# produkts = input("Ievadiet produkta nosaukumu ")
# if produkts == "Briseles kaposti":
#     print("Balastvielu daudzums uz 100g ir 4,4")
# if produkts == "Seleriju saknes":
#     print("Balastvielu daudzums uz 100g ir 4,2")
# if produkts == "Brokoli":
#     print("Balastvielu daudzums uz 100g ir 3,0")
# if produkts == "Ziedkaposti":
#     print("Balastvielu daudzums uz 100g ir 2,9")
# if produkts == "Burkani":
#     print("Balastvielu daudzums uz 100g ir 2,9")
# if produkts == "Sarkanas bietes":
#     print("Balastvielu daudzums uz 100g ir 2,5")
# if produkts == "Salati":
#     print("Balastvielu daudzums uz 100g ir 1,8")
# if produkts == "Upenes":
#     print("Balastvielu daudzums uz 100g ir 6,8")
# if produkts == "Avenes":
#     print("Balastvielu daudzums uz 100g ir 5,0")
# if produkts == "Zemenes":
#     print("Balastvielu daudzums uz 100g ir 4,0")
# if produkts == "Janogas":
#     print("Balastvielu daudzums uz 100g ir 2,5")
# if produkts == "Aboli":
#     print("Balastvielu daudzums uz 100g ir 2,3")
# if produkts == "Apelsini":
#     print("Balastvielu daudzums uz 100g ir 2,2")
# if produkts == "Plumes":
#     print("Balastvielu daudzums uz 100g ir 1,7")

#2.uzdevums
# vards = input("Ievadi tekstu")
# patskani = "aeiouAEIOU"
# rezultats = ""
# for letters in vards:
#     if letters not in patskani:
#         rezultats += letters

# print("vards bez patskaniem:", rezultats)

#3.uzdevums
cena=90
summa=0
nauda=[5, 10, 20, 50]
while summa < cena:
    ievadita_moneta = int(input("Ievietojiet naudu 5, 10, 20 vai 50 centi: "))
if ievadita_moneta in nauda:
    summa += ievadita_moneta
    print(f"Paslaik ievietota summa: {summa} centi")
else:
    print("nederiga moneta, ludzu ievietojiet 5, 10 ,20, 50 centus.")
atlikums = summa - cena
if atlikums > 0:
    print(f"Jaizdot {atlikums} centi.")
