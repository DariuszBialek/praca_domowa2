# Program do obsługi bazy szkolnej

# baza danych uczniów nauczycieli i wychowawców
import pprint
baza_uzyt = {
    "uczniowie": [
        {
         "imię": "Jan",
         "nazwisko": "Kowalski",
         "klasa": "1A"
         },
        {
         "imię": "Anna",
         "nazwisko": "Nowak",
         "klasa": "1A"
         },
        {
         "imię": "Janusz",
         "nazwisko": "Ptak",
         "klasa": "2C"
         }],
    "nauczyciele":
        [{"imię": "Adam", "nazwisko": "Malysz", "przedmiot": "Dekarstwo", "klasa": ["1A", "2C"]},
        {"imię": "Mariusz", "nazwisko": "Maliszewski", "przedmiot": "Dekarstwo", "klasa": ["1A", "2C"]},
        {"imię": "Karol", "nazwisko": "Pudzianowski", "przedmiot": "WF", "klasa": ["1A"]}],
    "wychowawcy":
        [{
         "imię": "Jan",
         "nazwisko": "Pszczola",
         "klasa": "1A"
         },
        {
         "imię": "Maria",
         "nazwisko": "Majewska",
         "klasa": "2C"
        }
        ],}

def utworz_uzytkownika(typ_uzytkownika):
    if typ_uzytkownika == "uczen":
        print("tworzenie ucznia")
        imie = input("podaj imię")
        nazw = input("podaj nazwisko")
        kl = input("podaj klasę")
        baza_uzyt["uczniowie"].append({"imię": imie, "nazwisko":nazw, "klasa":kl})

    elif typ_uzytkownika == "nauczyciel":
        print("tworzenie nauczyciela")
        lista_klas = []
        imie = input("podaj imię")
        nazw = input("podaj nazwisko")
        przedm = input("podaj_przedmiot")
        kl = input("podaj klasę: ")
        while kl != "":
            lista_klas.append(kl)
            kl = input("podaj klasę: ")
        baza_uzyt["nauczyciele"].append({
            "imię": imie,
            "nazwisko": nazw,
            "przedmiot": przedm,
            "klasa": lista_klas
        })

        baza_uzyt["uczniowie"].append({"imię": imie, "nazwisko":nazw, "klasa":kl})

    elif typ_uzytkownika == "wychowawca":
        print("tworzenie wychowawcy")
        imie = input("podaj imię")
        nazw = input("podaj nazwisko")
        kl = input("podaj klasę")
        baza_uzyt["wychowawcy"].append({"imię": imie, "nazwisko":nazw, "klasa":kl})
    elif typ_uzytkownika == "debug":
        pprint.pprint(baza_uzyt)

    else:
        print("nieprawidłowe dane")

def zarzadzanie_uzyt(polecenie):
    if polecenie == "klasa":
        print("informację o klasie")
#
        nazwa_klasy = input("Podaj nazwę klasy: ")
        uczniowie = []
        wychowawca = ""
        for uczen in baza_uzyt["uczniowie"]:
            if uczen["klasa"] == nazwa_klasy:
                uczniowie.append(uczen["imię"] + " " + uczen["nazwisko"])
        for wychow in baza_uzyt["wychowawcy"]:
            if wychow["klasa"] == nazwa_klasy:
                wychowawca = wychow["imię"] + " " + wychow["nazwisko"]
        print("Uczniowie: ", uczniowie)
        print("Wychowawca: ", wychowawca)
 #

    elif polecenie == "nauczyciel":
        print("informację o nauczycielach")
#
        imie_nauczyciela = input("Podaj imię nauczyciela: ")
        nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela: ")
        klasy = []
        for nauczyciel in baza_uzyt["nauczyciele"]:
            if nauczyciel["imię"] == imie_nauczyciela and nauczyciel[
                "nazwisko"] == nazwisko_nauczyciela:
                klasy.extend(nauczyciel["klasa"])
        print("Klasy: ", list(set(klasy)))
#

    elif polecenie == "wychowawca":
        print("informację o wychowawcach")

#
        imie_wychowawcy = input("Podaj imię wychowawcy: ")
        nazwisko_wychowawcy = input("Podaj nazwisko wychowawcy: ")
        uczniowie = []
        for klasa in baza_uzyt["wychowawcy"]:
            if klasa["imię"] == imie_wychowawcy and klasa[
                "nazwisko"] == nazwisko_wychowawcy:
                for uczen in baza_uzyt["uczniowie"]:
                    if uczen["klasa"] == klasa["klasa"]:
                        uczniowie.append(
                            uczen["imię"] + " " + uczen["nazwisko"])
        print("Uczniowie: ", uczniowie)
#

    elif polecenie == "uczen":
        print("informację o uczniach")
#
        imie = input("Podaj imię ucznia: ")
        nazwisko = input("Podaj nazwisko ucznia: ")
        for uczen in baza_uzyt["uczniowie"]:
            if uczen["imię"] == imie and uczen["nazwisko"] == nazwisko:
                klasa = uczen["klasa"]
                for wychowawca in baza_uzyt["wychowawcy"]:
                    if wychowawca["klasa"] == klasa:
                        print(f"Klasa: {klasa}, Wychowawca: {wychowawca['imię']} {wychowawca['nazwisko']}")
                return
        print("Nie znaleziono ucznia o podanych danych.")
#
    elif opcja == "debug":
        pprint.pprint(baza_uzyt)
    else:
        print("błedne polecenie")


opcja = ""
while opcja != "koniec":
   print("\nWitaj w systemie bazy szkolnej")
   print("dostępne opcje:")
   print("utworz")
   print("zarzadzaj")
   print("koniec")
   opcja = input("\nwybierz opcję")

   if opcja == "utworz":
        print("\nWybierz opcję:")
        print("uczen")
        print("wychowawca")
        print("nauczyciel")
        print("koniec")
        opcja_utworz = ""
        while opcja_utworz != "koniec":
            opcja_utworz = input("podaj typ użytkownika")
            utworz_uzytkownika(opcja_utworz)

   elif opcja == "zarzadzaj":
       opcja_zarzadzaj = ""
       while opcja_zarzadzaj != "koniec":
           opcja_zarzadzaj = input("podaj opcję: klasa, uczen, wychowawca, nauczyciel, koniec")
           if opcja_zarzadzaj == "koniec":
               break
           zarzadzanie_uzyt(opcja_zarzadzaj)


def klasa():
    nazwa_klasy = input("Podaj nazwę klasy: ")
    uczniowie = []
    wychowawca = ""
    for uczen in baza_uzyt["uczniowie"]:
        if uczen["klasa"] == nazwa_klasy:
            uczniowie.append(uczen["imię"] + " " + uczen["nazwisko"])
    for wychow in baza_uzyt["wychowawcy"]:
        if wychow["klasa"] == nazwa_klasy:
            wychowawca = wychow["imię"] + " " + wychow["nazwisko"]
    print("Uczniowie: ", uczniowie)
    print("Wychowawca: ", wychowawca)
