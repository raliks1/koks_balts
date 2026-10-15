class Skololotājs:
    def __init__(self, stundu_skaits_nedela, skolotaju_tips):
        self.stundu_skaits_nedela = stundu_skaits_nedela
        self.skolotaju_tips = skolotaju_tips

    def skolotaja_tips(self):
        if self.skolotaja_tips == 1:
            return "Sākumskolas skolotājs"
        else:
            return "Vidusskolas skolotājs"



class SākumskolasSkolotājs(Skololotājs):
    def __init__(self, stundu_skaits_nedela, skolotaju_tips, Uzvards, skolotaja_klase):
        super().__init__(stundu_skaits_nedela, skolotaju_tips)
        self.Uzvards = Uzvards
        self.skolotaja_klase = skolotaja_klase

    def ievadi_datus(self):
        self.uzvards = input("Ievadi Sākumskolas skolotāja uzvārdu: ")
        self.skolotaja_klase = input("Ievadi Sākumskolas skolotāja klasi: ")
        self.stundu_skaits_nedela = int(input("Ievadi stundu skaitu nedēļā: "))

class VidusskolasSkolotājs(Skololotājs):
    def __init__(self, pirmā_prieksmeta_nosuakums, otra_prieksmeta_nosaukums, pirma_prieksmeta_stundu__skaits, otra_prieksmeta_stundu_skaits):
        self.pirmā_prieksmeta_nosuakums = pirmā_prieksmeta_nosuakums
        self.otra_prieksmeta_nosaukums = otra_prieksmeta_nosaukums
        self.pirma_prieksmeta_stundu__skaits = pirma_prieksmeta_stundu__skaits
        self.otra_prieksmeta_stundu_skaits = otra_prieksmeta_stundu_skaits

    def ievadi_datus(self):
        self.uzvards = input("Ievadi Vidusskolas skolotāja uzvārdu: ")
        self.pirmā_prieksmeta_nosuakums: str = input("Ievadi pirmā priekšmeta nosaukumu: ")
        self.otra_prieksmeta_nosaukums = input("Ievadi otrā priekšmeta nosaukumu: ")
        self.pirma_prieksmeta_stundu__skaits = int(input("Ievadi pirmā priekšmeta stundu skaitu nedēļā: "))
        self.otra_prieksmeta_stundu_skaits = int(input("Ievadi otrā priekšmeta stundu skaitu nedēļā: "))

if __name__ == "__main__":
    skolotajs1 = SākumskolasSkolotājs(0, 1, "", "")
    skolotajs1.ievadi_datus()
    print(f"Sākumskolas skolotāja uzvārds: {skolotajs1.uzvards}, stundu skaits nedēļā: {skolotajs1.stundu_skaits_nedela}, Skolotāja klase: {skolotajs1.skolotaja_klase}")

    skolotajs2 = VidusskolasSkolotājs("", "", 0, 0)
    skolotajs2.ievadi_datus()
    print(f"Vidusskolas skolotāja priekšmeti: {skolotajs2.pirmā_prieksmeta_nosuakums} ({skolotajs2.pirma_prieksmeta_stundu__skaits} stundas nedēļā), {skolotajs2.otra_prieksmeta_nosaukums} ({skolotajs2.otra_prieksmeta_stundu_skaits} stundas nedēļā), kopā {skolotajs2.pirma_prieksmeta_stundu__skaits + skolotajs2.otra_prieksmeta_stundu_skaits} stundas nedēļā.")