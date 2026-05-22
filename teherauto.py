from auto import Auto


class Teherauto(Auto):

    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.__teherbiras = teherbiras

    @property
    def teherbiras(self):
        return self.__teherbiras

    def __str__(self):
        return f"Teherautó - {super().__str__()} - {self.teherbiras} kg"