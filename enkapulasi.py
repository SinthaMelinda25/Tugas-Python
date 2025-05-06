class Buku:
    def __init__(self, judul, penulis):
        self._judul = judul # Private attribute
        self.penulis = penulis

    def info(self):
        print(f"Judul: {self._judul}, Penulis: {self.penulis}")

b1 = Buku("Python Dasar", "Budi")
b1.info()