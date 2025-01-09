import os
os.system('cls') #attira terminala logu pasa sakuma
print("\n") # ieliek tuksu rindinu pirms izdrukas

skolens = ["Viktorija", "Artūrs", "Džošuo", "Roberts"]
# print(skolens)

# print(skolens[1])
# print(skolens[2])
# print(skolens[0])

# for sk in  skolens:
#     print(sk)

# skola = "25.vidusskola"
# for burts in skola:
#     print(burts)

# for i in range(len(skolens)):
#     print(i + 1,skolens[i])

# skolotajs = ["Gustava", "Ungure", "Deksne", "Gladčenko"]
# macibu_prieksmets = ["matematika", "matematika", "matematika", "fizika"]

# skolotajs = {
#     "Gustava": "matematika", 
#     "Ungure": "matematika",
#     "Deksne": "matematika",
#     "Gladčenko": "fizika",
# }

# print(skolotajs["Deksne"])
# print(skolotajs["Gladčenko"])

# for skol in skolotajs:
#     print(skol, skolotajs[skol], sep=" maca ")










# skolotajs = [
#         {"uzvards": "Gustava", "macibu_prieksmets": "matematika", "kabinets": "27."},
#         {"uzvards": "Ungure", "macibu_prieksmets": "matematika", "kabinets": "205."},
#         {"uzvards": "Deksne", "macibu_prieksmets": "matematika", "kabinets": None},
#         {"uzvards": "Gladčenko", "macibu_prieksmets": "fizka", "kabinets": "206."}
#     ]

# for skol in skolotajs:
#     print(skol["uzvards"], skol["macibu_prieksmets"], skol["kabinets"], sep=", ")

platums = int(input("platums- "))
augstums = int(input("augstums- "))

for i in range(augstums):
    for j in range(platums):
        print("@", end="")
    print()
