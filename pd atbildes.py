#string = input("Ievadi simbolu virkni: ")
#print(f"Simbolu virknes garums: {len(string)}")

#print(f"Simbolu virknes garums: {string.lower()}")
#print(f"Simbolu virknes garums: {string.upper()}")
 
#symbol = input("Ievadi simbolu, ko lietot tukšo vietu aizvietošanai: ")
#print(f"Simbolu virknes garums: {string.replace(' ',symbol)}")

#word_to_check = "Python"
#print(f"Vai virkne satur vārdu '{word_to_check}'? {'Python' in string}")

#print(f"Pirmie pieci simboli: {string[:5]}")
#print(f"Pēdējie trīs simboli: {string[:-3]}")

number = float(input("Ievadi skaitli: "))
print(f"Skaitlis noapaļots līdz diviem cipariem aiz komata: {round(number,2)}")

integer = int(input("Ievadi veselu skaitli: "))
print(f"Skaitlis kā decimāldaļā: {float(integer)}")

large_number = int(input("Ievadi lielu skaitli: "))
print("skaitlis ar tukstoš atdalītāju: {large_number:,}".replace(',' ' '))

print(f"Skaitlis binārajā sistēmā: {bin(integer)[2:]}")
print(f"Skaitlis oktālajā sistēmā: {oct(integer)[2:]}")
print(f"Skaitlis heksidecimālajā sistēmā: {hex(integer)[2:]}")

negative_number = int(input("Ievadi negatīvo skaitli: "))
print(f"Absolūtā vērtība: {abs(negative_number)}")