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

line_count = 0
with open('data.txt', 'r') as file:
    for line in file:
        line_count += 1
print("kopā līnijas:", line_count)

# 3. Vārda sastopamības skaitīšana failā

# file = open("Data.txt", "w") 

# vārds = input("Ievadi tekstu: ") 
# file.write(vārds) 
# file.write("\n") 
    
# file.close()

# text = open("Data.txt", "r") 
# d = dict() 
# for line in text: 
# 	line = line.strip() 
# 	line = line.lower() 
# 	words = line.split(" ") 	
# 	for word in words: 
# 		if word in d: 
# 			d[word] = d[word] + 1
# 		else: 
# 			d[word] = 1
# for key in list(d.keys()): 
# 	print(key, ":", d[key]) 

# 4. Datu pievienošana failam 

# 5. Apvienot divus failus, pārmaiņus ierakstot rindas






# 6. Vārdu atkārtošanās skaita noteikšana failā

# 7. Studentu atzīmju analīze no faila

# 8. Liela faila apstrāde un analīze (Augstāks līmenis)

# 9. Faila filtrēšana un jauna faila izveide (Augstāks līmenis)

# 10. Ezeru saraksta izveide RTF failā