string = input("Ievadi simbolu virkni: ")
print(f"Simbolu virknes garums: {len(string)}")

print(f"Simbolu virknes garums: {string.lower()}")
print(f"Simbolu virknes garums: {string.upper()}")
 
symbol = input("Ievadi simbolu, ko lietot tukšo vietu aizvietošanai: ")
print(f"Simbolu virknes garums: {string.replace(' ',symbol)}")

word_to_check = "Python"
print(f"Vai virkne satur vārdu '{word_to_check}'? {'Python' in string}")