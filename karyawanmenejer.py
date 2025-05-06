class karyawan:
    salam1 = "karyawan" 
    salam2 = "menejer" 
    def salam(self):
        print(f"Halo,saya {self.salam1}")

class menejer(karyawan):
    def salam(self):
        print(f"Halo,saya {self.salam2}")

k = karyawan()
k.salam()
m = menejer()
m.salam()