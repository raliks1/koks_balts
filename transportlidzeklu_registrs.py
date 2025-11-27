import os
os.system('cls')
print("\n")

class Transprotlddzeklis:
    def __init__(self, marka, gads):
        self.marka = marka
        self.gads = gads

    def info(self):
        print(f"Marka: {self.marka}, Gads: {self.gads}")
class Auto(Transprotlddzeklis):
    def __init__(self, marka, gads, durvju_skaits):
        super().__init__(marka, gads)
        self.durvju_skaits = durvju_skaits

    def durvis(self):
        print(f"Šim auto ir {self.durvju_skaits} durvis.")
Transprotlddzeklis1 = Transprotlddzeklis("Audi", 2008)
auto=Auto("BMW", 2015, 4)
Transprotlddzeklis1.info()
auto.durvis()
