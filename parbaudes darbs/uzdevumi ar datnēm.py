import os
os.system('cls')
print("\n")

# 1. Vienkārša teksta rakstīšana un lasīšana no faila 

# file = open("Teksts.txt", "w") 

# vārds = input("Ievadi tekstu: ") 
# file.write(vārds) 
# file.write("\n") 
    
# file.close() 

# print("Teksts ir ierakstīts failā") 

# 2. Rindu skaitīšana failā
 
# with open('data.txt', 'r', encoding = "utf-8") as file:
#     x = len(file.readlines())
#     print(x)

# 3. Vārda sastopamības skaitīšana failā

vards = input("ievadi vārdu:").upper()
with open('vardi.txt', 'r', encoding="utf-8") as data:
    x = data.readlines()
mekl = x.count(vards + "\n")
print(f"{vards} parādās {mekl}")

# 4. Datu pievienošana failam 
# import datetime

# file = open("logs.txt", "+a") 

# vārds = input("Ievadi tekstu: ") 
# file.write(vārds) 
# file.write("\n") 
    
# file.close() 

# 5. Apvienot divus failus, pārmaiņus ierakstot rindas

# 6. Vārdu atkārtošanās skaita noteikšana failā

# 7. Studentu atzīmju analīze no faila

# 8. Liela faila apstrāde un analīze (Augstāks līmenis)

# 9. Faila filtrēšana un jauna faila izveide (Augstāks līmenis)

# 10. Ezeru saraksta izveide RTF failā