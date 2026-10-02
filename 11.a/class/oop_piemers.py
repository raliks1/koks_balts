import os
os.system('cls')
print("\n")

# kaka_vards = "Runcis"
# kaka_krasa = "orandzs"

# def naudet(vards):
#     print(f"{vards} sāk njaudēt latviski - njau-njau! ")

# naudet(kaka_vards)

# class kakis:
#     name = ""
#     suga = ""
#     vecums = 0

# #konstruktors
# kakis1 = kakis()
# kakis1.name = "Murka"
# kakis1.suga = "Persiešu"
# kakis1.vecums = 3

# kakis2 = kakis()
# kakis2.name = "Runcis"
# kakis2.suga = "Sibīrijas"
# kakis2.vecums = 5

# print(f"Pirmais kakis - vārds: {kakis1.name}, suga: {kakis1.suga}, vecums: {kakis1.vecums} gadi")
# print(f"Otrais kakis - vārds: {kakis2.name}, suga: {kakis2.suga}, vecums: {kakis2.vecums} gadi")

# class Persona:
#     def __init__(self, vards, vecums):
#         self.vards = vards
#         self.vecums = vecums
#     def sveicinaties(self):
#         print(f"Sveiki, mani sauc {self.vards} un man ir {self.vecums} gadi.")

# janis = Persona("Janis", 30)
# peteris = Persona("Peteris", 25)

# janis.sveicinaties()
# peteris.sveicinaties()

# class Printers:
#     def drukat(self):
#         print("Drukājam dokumentu...")

# skolas_printeris = Printers()

# skolas_printeris.drukat()

# class Skaititajs:
#     def skaitli(self, n):
#         for i in range(1, n + 1):
#             print(i)

# skaitlis = Skaititajs()

# skaits = int(input("Ievadi skaitli līdz kuram skaitīt: "))

# skaitlis.skaitli(skaits)

# 1. konstruktors un 2. īpašības
# class Dators:
#     def __init__(self, modelis, ram_gb):
#         self.modelis = modelis
#         self.ram_gb = ram_gb

#     # 3. metode
#     def parbaudi_speju(self):
#             if self.ram_gb >= 16:
#                return "Lieliska spējīgs!"
#             else:
#                return "Der vienkāršiem darbiem."\

# # Objektu izvēle            
# mans_dators = Dators("Windows 11", 32)
# skolnieka_dators = Dators("Windows 10", 8)

# # Metodes izsaukšana
# print(f"{mans_dators.modelis} (RAM: {mans_dators.ram_gb} GB): {mans_dators.parbaudi_speju()}")
# print(f"{skolnieka_dators.modelis} (RAM: {skolnieka_dators.ram_gb} GB): {skolnieka_dators.parbaudi_speju()}")
# 1. bāzes klase
class Dzīvnieks:
    def __init__(self, vards):
        self.vards = vards

    def est(self):
        print(f"{self.vards} ēd ")
# 2. BĒRNU KLASE (mantotā klase)
#Suns mantos visas Dzīvnieka īpašības un metodes
class Suns(Dzīvnieks):
    def riet(self):
        print(f"{self.vards} saka: Vau-vau!")

        #piezīmes: Sunim nav jādefinē __init__ vai est(), jo tas to manto!

#objekta izveide
dog = Suns("Lācis")

# 3. mantošanas izmantošana


#izmanto metodi no Vecāklases (Dzīvnieks)
dog.est()        #Izvade : Lācis ēd.

#izmantometodi no savas klases (Suns)
dog.riet()      #Izvade : Lācis saka: Vau-vau!


        
