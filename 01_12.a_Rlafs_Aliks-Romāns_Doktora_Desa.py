class Doktoraats:
    def __init__(self, doktoraata_nosuakums="", Doktoraata_pacientu_skaits=0):
        self.doktoraata_nosaukums = doktoraata_nosuakums
        self.Doktoraata_pacientu_skaits = Doktoraata_pacientu_skaits

    def ievadi_datus(self):
        self.doktoraata_nosaukums = input("Ievadi doktoraāta nosaukumu: ")
        self.Doktoraata_pacientu_skaits = int(input("Ievadi pacientu skaitu: "))

    def iegust_datus(self):
       return self.doktoraata_nosaukums, self.Doktoraata_pacientu_skaits

if __name__ == "__main__":
    mans_doktoraats = Doktoraats()
    mans_doktoraats.ievadi_datus()
    print("Doktarāts", mans_doktoraats.doktoraata_nosaukums, "apkalpo", mans_doktoraats.Doktoraata_pacientu_skaits, "pacientus.")
    