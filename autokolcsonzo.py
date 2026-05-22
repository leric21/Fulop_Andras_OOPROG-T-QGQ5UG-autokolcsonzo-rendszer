from berles import Berles


class Autokolcsonzo:

    def __init__(self, nev):
        self.__nev = nev
        self.__autok = []
        self.__berlesek = []

    @property
    def nev(self):
        return self.__nev

    @property
    def autok(self):
        return self.__autok

    @property
    def berlesek(self):
        return self.__berlesek

    def auto_hozzaadas(self, auto):
        self.__autok.append(auto)

    def berles_hozzaadas(self, auto, datum, berlo_nev):

        for berles in self.__berlesek:
            if berles.auto.rendszam == auto.rendszam and berles.datum == datum:
                raise Exception("Az autó már foglalt erre a napra!")

        uj_berles = Berles(auto, datum, berlo_nev)
        self.__berlesek.append(uj_berles)

        return auto.berleti_dij

    def berles_lemondas(self, rendszam, datum):

        for berles in self.__berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.__berlesek.remove(berles)
                return

        raise Exception("Nem található ilyen bérlés!")

    def berlesek_listazasa(self):

        if len(self.__berlesek) == 0:
            print("Nincs aktív bérlés.")
            return

        for berles in self.__berlesek:
            print(berles)