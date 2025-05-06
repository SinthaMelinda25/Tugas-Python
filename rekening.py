class rekeningbank:
    def __init__(self,saldo):
        self.__saldo = saldo
    def lihatsaldo(self):
        print(f"kamu mempunyai saldo sebanyak {self.__saldo}")
    def tambahsaldo(self,jumlah):
        self.__saldo += jumlah
        print(f"saldo anda ditambahkan {jumlah}")
    def tariksaldo(self,jumlah):
        self.__saldo -= jumlah
        print(f"saldo anda ditarik {jumlah}")

r = rekeningbank(1000000)
r.lihatsaldo()
r.tariksaldo(500000)
r.tambahsaldo(20000)
r.lihatsaldo()
