class Hewan:
    def __init__(self,nama):
        self.nama = nama
        self.nama = nama
    def suara(self):
            print("Hewan bersuara")

class Kucing(Hewan):
    def suara(self):
         print(f"{self.nama} Meong")

class Domba(Hewan):
    def suara(self):
        print(f"{self.nama} Mbeeeeeee")

h = Hewan("hewan umum")
h.suara()

k = Kucing("kucing")
k.suara()

d = Domba("domba")
d.suara()