class Berles:

    def __init__(self, auto, datum, berlo_nev):
        self.__auto = auto
        self.__datum = datum
        self.__berlo_nev = berlo_nev

    @property
    def auto(self):
        return self.__auto

    @property
    def datum(self):
        return self.__datum

    @property
    def berlo_nev(self):
        return self.__berlo_nev

    def __str__(self):
        return f"{self.auto.tipus} ({self.auto.rendszam}) - {self.datum} - Bérlő: {self.berlo_nev}"