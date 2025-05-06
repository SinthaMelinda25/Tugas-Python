class Ayah:
        bentuktubuh = "berisi"
        rambut = "lurus"
        bentukwajah = "bulat"
        alis = "tebal"
        mata = "sipit"
        def warisan(self):
              print("KARAKTERISTIK YANG DIWARISKAN OLEH AYAH")
            

class saya(Ayah):
        def tubuh(self):
              print(f"ayah saya mewariskan bentuk tubuh yang {self.bentuktubuh} kepada saya")
        def gayarambut(self):
            print(f"ayah saya mewariskan rambut yang {self.rambut} kepada saya")
        def bentukmuka(self):
            print(f"ayah saya mewariskan bentuk wajah {self.bentukwajah} kepada saya")
        def bentukalis(self):
              print(f"ayah saya mewariskan alis {self.alis} kepada saya")
        def bentukmata(self):
              print(f"ayah saya mewariskan mata yang {self.mata} kepada saya")

class kakak(Ayah):
      def gayarambut(self):
            print(f"kakak diwarisi oleh ayah rambut yang {self.rambut} sama seperti saya")
      def bentukalis(self):
            print(f"kakak juga diwarisi alis yang {self.alis}")
      def bentukmuka(self):
            print(f"tetapi kakak saya tidak mempunyai warisan seperti bentuk muka bulat dan mata yang sipit")
      
Ayahsaya = Ayah()
Ayahsaya.warisan()

saya = saya()
saya.tubuh()
saya.gayarambut()
saya.bentukmuka()
saya.bentukalis()
saya.bentukmata()

ka = kakak()
ka.gayarambut()
ka.bentukalis()
ka.bentukmuka()
        