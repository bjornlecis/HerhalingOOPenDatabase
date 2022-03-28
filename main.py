class Voedsel:

    def __init__(self,idVoedsel,naam,kostprijs):
        self.idVoedsel = idVoedsel
        self.naam = naam
        self.kostprijs = kostprijs

    def __str__(self):
        return "id: {} naam {} kostprijs {}".format(self.idVoedsel,self.naam,self.kostprijs)

class Dier:

    def __init__(self,idDier,naam,soort,geslacht,voedsel):
        self.idDier = idDier
        self.naam = naam
        self.soort = soort
        self.geslacht = geslacht
        self.voedsel = voedsel

    def __str__(self):
        return "Dier ID: {} naam {} \nSoort {} Geslacht {}".format(self.idDier,self.naam,self.soort,self.geslacht)

class Verzorger:

    def __init__(self,idVerzorger,naam):
        self.idVerzorger = idVerzorger
        self.naam = naam
        self.lijstdieren = []
    def voeg_dier_toe(self,dier):
        self.lijstdieren().append(dier)
    def __str__(self):
        return "ID : {} Naam {}".format(self.idVerzorger,self.naam)


graan =  Voedsel("V1","graan",5)
hondenvoer = Voedsel("V2","Hondenbrokken",10)
d1 = Dier("d1","Blacky","Hond","V",hondenvoer)
d2 = Dier("d2","Toby","Hond","M",hondenvoer)


print(d1)
