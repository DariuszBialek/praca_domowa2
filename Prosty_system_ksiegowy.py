#Prosty system księgowy/magazyn
stan_konta = float(1000.00)
magazyn = {"mleko":{"cena":2.20, "ilosc":10},
           "chleb":{"cena":3.00, "ilosc":15},
           "maslo":{"cena":5.00, "ilosc":20}
           }
opcje = ["saldo", "sprzedaz", "zakup", "konto", "lista", "magazyn", "przeglad", "koniec"]
opcja = ()
historia_akcji = []
while opcja != "koniec":
    while opcja not in opcje:
        opcja = input("Wprowadź jedną z poniższych opcji:\n" + "\n".join(opcje) + "\n")
        print(f"wprowadziłeś: {opcja}")
        if opcja not in opcje:
            print("Niepoprawna opcja.")
    if opcja == "koniec":
        break

#sprzedaż
    if opcja == "sprzedaz":
        print(f"produkty dostepne na magazynie: {magazyn}") #{list(magazyn.keys())}")
        magazyn_set = set(magazyn.keys())
        sprzedaz_produkt = ""
        while sprzedaz_produkt not in magazyn_set:
            sprzedaz_produkt = input("wprowadz nazwę produktu")
            if sprzedaz_produkt not in magazyn_set:
                print("brak produktu na magazynie")

        sprzedaz_cena = float(input("wprowadz cenę jednostkową produktu"))
        sprzedaz_ilosc = int(input("wprawadz ilość sprzedawanych produktów"))
        if sprzedaz_ilosc > magazyn[sprzedaz_produkt]["ilosc"]:
            print("brak wystarczajacej ilości produktów na magazynie")
            print(stan_konta)
        if sprzedaz_ilosc <= magazyn[sprzedaz_produkt]["ilosc"]:
            magazyn[sprzedaz_produkt]["ilosc"] -= sprzedaz_ilosc
            stan_konta += sprzedaz_ilosc * sprzedaz_cena
            historia_akcji.append(f"{opcja}{sprzedaz_ilosc}{sprzedaz_cena}PLN")
            print(f"SPRZEDANO: {sprzedaz_produkt} SZT. {sprzedaz_ilosc} W CENIE {sprzedaz_cena} SALDO {stan_konta}"
                  f"\nNACISNIJ ENTER ABY PRZEJSC DO GŁÓWNEGO MENU")
            input()
            opcja = ""

#zakup
    if opcja == "zakup":
        print(f"produkty dostepne na magazynie: {magazyn}") #{list(magazyn.keys())}")
        magazyn_set = set(magazyn.keys())
        zakup_produkt = input("wprowadz nazwę kupowanego produktu")
        zakup_cena = float(input("wprowadz jednostkową cenę zakupu produktu"))
        zakup_ilosc = int(input("wprowadza ilość zakupionych produktów"))
        if zakup_produkt in magazyn_set and ((zakup_cena * zakup_ilosc) <= stan_konta):
            magazyn[zakup_produkt]["ilosc"] += zakup_ilosc
            stan_konta -= (zakup_cena * zakup_ilosc)
            print(f"zakupiono {zakup_produkt} SZT.:{zakup_ilosc} W CENIE {zakup_cena}PLN\nPRZECHODZĘ DO GŁÓWNEGO MENU")
            historia_akcji.append(f"{opcja} {zakup_produkt} {zakup_cena}PLN {zakup_ilosc}SZT.")
        elif zakup_produkt not in magazyn_set and ((zakup_cena * zakup_ilosc) <= stan_konta):
            magazyn[zakup_produkt] = {"cena": zakup_cena, "ilosc": zakup_ilosc}
            historia_akcji.append(f"{opcja} {zakup_produkt} {zakup_cena}PLN {zakup_ilosc}SZT.")
            stan_konta -= (zakup_cena * zakup_ilosc)
        else:
            print("niewystarczająca ilość PLN")
        print("NACISNIJ ENTER ABY PRZEJSC DO GŁÓWNEGO MENU")
        input()
        opcja = ""

#saldo
    if opcja == "saldo":
        saldo_opcje = ["+", "-", "wyjscie"]
        saldo_akcja = ()
        while saldo_akcja not in saldo_opcje:
            saldo_akcja = input("Wprowadź jedno z 3 możliwych działań:\n" + "\n".join(saldo_opcje) + "\n")
        if saldo_akcja == "wyjscie":
            opcja = ""
            print("PRZECHODZĘ DO GŁÓWNEGO MENU")
            while opcja not in opcje:
                opcja = input(
                    "Wprowadź jedną z poniższych opcji:\n" + "\n".join(opcje) + "\n")
                print(f"wprowadziłeś: {opcja}")
                if opcja not in opcje:
                    print("Niepoprawna opcja.")
        elif saldo_akcja != "wyjscie":
            print(saldo_akcja)
            kwota_akcja = input("podaj kwotę operacji")
            if saldo_akcja == "-":
                stan_konta = stan_konta - float(kwota_akcja)
                print(stan_konta)
                historia_akcji.append(f"{opcja}{saldo_akcja}{kwota_akcja}PLN")
            elif saldo_akcja == "+":
                stan_konta += float(kwota_akcja)
                print(stan_konta)
                historia_akcji.append(f"{opcja}{saldo_akcja}{kwota_akcja}PLN")
#konto
    if opcja == "konto":
        konto_opcje = ["stan konta", "wyjscie"]
        konto_akcja = ()
        while konto_akcja not in konto_opcje:
            konto_akcja = input("Wprowadź jedno z 2 możliwych działań:\n" + "\n".join(konto_opcje) + "\n")
        if konto_akcja != "wyjscie":
           print(stan_konta)
           historia_akcji.append(f"sprawdzenie stanu konta{stan_konta}PLN")
        else:
            opcja = ""
            print("PRZECHODZĘ DO GŁÓWNEGO MENU")
#magazyn
    if opcja == "magazyn":
        magazyn_produkt = input("wprowadz nazwę produktu")
        if magazyn_produkt in magazyn:
            print(f"{magazyn_produkt}{magazyn[magazyn_produkt]}\nNACISNIJ ENTER ABY PRZEJSC DO GŁÓWNEGO MENU")
        elif magazyn_produkt not in magazyn:
            print(f"BRAK {magazyn_produkt} W MAGAZYNIE\nNACISNIJ ENTER ABY PRZEJSC DO GŁÓWNEGO MENU")
        input()
        opcja = ""
#lista
    if opcja == "lista":
        print("magazyn")
        for lista_produkt, dane_produkt in magazyn.items():
            print(f"{lista_produkt} {dane_produkt['cena']} {dane_produkt['ilosc']}")
        print("nacisnij ENTER aby kontynuować")
        input()
        opcja = ""

#przeglad
    if opcja == "przeglad":
        print(f"podaj zakres do wyswietlenia, cała historia to lp=0 do lp={len(historia_akcji)}")
        historia_od = int(input("podaj pozycję od której chcesz wyświetlić historię"))
        while historia_od < 0 or historia_od > (len(historia_akcji) + 1):
            historia_od = int(input("wprowadziłeś lp. z poza zakresu historii, "
                                    "podaj pozycję od której chcesz wyświetlić historię"))

        historia_do = int(input("podaj pozycję do której chcesz wyświetlić historię"))
        while historia_do < historia_od or historia_do > (len(historia_akcji) + 1):
            historia_do = int(input("wprowadziłeś nieprawidłowy zakresu historii do, "
                                    "podaj pozycję do której chcesz wyświetlić historię"))
        print("\n".join(historia_akcji[historia_od:historia_do]))
        print("nacisnij ENTER aby kontynuować")
        input()
        opcja = ""
