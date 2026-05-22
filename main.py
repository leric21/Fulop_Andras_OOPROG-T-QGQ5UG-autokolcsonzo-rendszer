from datetime import datetime

from szemelyauto import Szemelyauto
from teherauto import Teherauto
from autokolcsonzo import Autokolcsonzo


kolcsonzo = Autokolcsonzo("Speed Rent")


auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 12000, 5)
auto2 = Szemelyauto("GHI-789", "BMW 320", 18000, 5)
auto3 = Teherauto("DEF-456", "Ford Transit", 20000, 3000)


kolcsonzo.auto_hozzaadas(auto1)
kolcsonzo.auto_hozzaadas(auto2)
kolcsonzo.auto_hozzaadas(auto3)


kolcsonzo.berles_hozzaadas(auto1, "2026-05-22", "Kiss Péter")
kolcsonzo.berles_hozzaadas(auto2, "2026-05-23", "Nagy Anna")
kolcsonzo.berles_hozzaadas(auto3, "2026-05-24", "Tóth Béla")
kolcsonzo.berles_hozzaadas(auto1, "2026-05-25", "Szabó József")


def auto_keresese(rendszam):

    for auto in kolcsonzo.autok:
        if auto.rendszam == rendszam:
            return auto

    return None


while True:

    print("\n===== AUTÓKÖLCSÖNZŐ RENDSZER =====")
    print("1 - Autó bérlése")
    print("2 - Bérlés lemondása")
    print("3 - Bérlések listázása")
    print("4 - Elérhető autók listázása")
    print("5 - Kilépés")

    valasztas = input("Válassz egy menüpontot: ")

    if valasztas == "1":

        try:

            rendszam = input("Add meg az autó rendszámát: ")
            datum = input("Add meg a dátumot (YYYY-MM-DD): ")
            berlo_nev = input("Add meg a bérlő nevét: ").strip()

            if not berlo_nev:
                raise Exception("A bérlő neve nem lehet üres!")

            datetime.strptime(datum, "%Y-%m-%d")

            auto = auto_keresese(rendszam)

            if auto is None:
                raise Exception("Nincs ilyen rendszámú autó!")

            ar = kolcsonzo.berles_hozzaadas(auto, datum, berlo_nev)

            print(f"Sikeres bérlés! Fizetendő összeg: {ar} Ft")

        except ValueError:
            print("Hibás dátum formátum!")

        except Exception as hiba:
            print(f"Hiba: {hiba}")

    elif valasztas == "2":

        try:

            rendszam = input("Add meg a rendszámot: ")
            datum = input("Add meg a dátumot: ")

            kolcsonzo.berles_lemondas(rendszam, datum)

            print("Bérlés sikeresen lemondva.")

        except Exception as hiba:
            print(f"Hiba: {hiba}")

    elif valasztas == "3":

        print("\nAktív bérlések:\n")
        kolcsonzo.berlesek_listazasa()

    elif valasztas == "4":

        print("\nElérhető autók:\n")

        for auto in kolcsonzo.autok:
            print(auto)

    elif valasztas == "5":

        print("Kilépés...")
        break

    else:
        print("Érvénytelen menüpont!")