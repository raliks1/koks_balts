import os
os.system('cls')
print("\n")

class Cilveks:
    def __init__(self, vards, uzvards):
        self.vards = vards
        self.uzvards = uzvards
class Students(Cilveks):
    def __init__(self, vards, uzvards, kurss, atzime):
        super().__init__(vards, uzvards)
        self.kurss = kurss
        self.atzime = atzime

    def info(self):
        print(f"Vārds: {self.vards} {self.uzvards}, Kurss: {self.kurss}, Atzīme: {self.atzime}")


