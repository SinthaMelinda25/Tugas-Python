class lampu:
    def __init__(self):
        self.bentuk = "bulat"
        self.merek = "phillips" 
        self.warna = "putih"
        self.ukuran = "5 watt" 

    def mati(self):
        print("lampu mati")

    def nyala(self):
        print("lampu nyala")

lampu1 = lampu()
lampu1 = lampu()

lampu1.mati()
lampu1.nyala()

