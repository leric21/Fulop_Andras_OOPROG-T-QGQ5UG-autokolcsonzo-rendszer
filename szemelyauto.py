from auto import Auto


class Szemelyauto(Auto):

    def __init__(self, rendszam, tipus, berleti_dij, ajtok_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.__ajtok_szama = ajtok_szama

    @property
    def ajtok_szama(self):
        return self.__ajtok_szama

    def __str__(self):
        return f"Személyautó - {super().__str__()} - {self.ajtok_szama} ajtó"