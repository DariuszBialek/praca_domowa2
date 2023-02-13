print("Pętle i argumenty w konsoli")
element = int(input("podaj liczbe elementów które chcesz wysłac:"))
i = element
lista_elementow = []
numery_paczek = []
waga_paczek = []
najlzejsze_paczki = []
puste_kilogramy = []
wagi_elementów = []
numer_paczki = 0
najlzejsza_paczka = 0

for element in range(1,element+1):
        waga_elementu = float(input(f"podaj wagę {element} elementu"))

        if ((waga_elementu >= 1) and (waga_elementu <= 10)):
            wagi_elementów.append(waga_elementu)
            if ((waga_elementu + sum(lista_elementow)) < 20) and element < i:
                lista_elementow.append(waga_elementu)
                waga_paczki = sum(lista_elementow)

            elif ((waga_elementu + sum(lista_elementow)) == 20) and element < i:
                lista_elementow.append(waga_elementu)
                waga_paczki = sum(lista_elementow)
                numer_paczki = numer_paczki + 1
                waga_paczek.append(waga_paczki)
                print(f"paczka {numer_paczki} o wadze {waga_paczki}kg została spakowana")
                lista_elementow.clear()

            elif ((waga_elementu + sum(lista_elementow)) <= 20) and element == i:
                lista_elementow.append(waga_elementu)
                waga_paczki = sum(lista_elementow)
                numer_paczki = numer_paczki + 1
                waga_paczek.append(waga_paczki)
                print(f"paczka: {numer_paczki} o wadze: {waga_paczki} została spakowana")

            elif ((waga_elementu + sum(lista_elementow)) > 20) and element < i:
                numer_paczki = numer_paczki + 1
                print(f"paczka: {numer_paczki} o wadze: {waga_paczki} została spakowana, element {element} został dodany do kolejnej paczki")
                numery_paczek.append(numer_paczki)
                waga_paczek.append(waga_paczki)
                lista_elementow.clear()
                lista_elementow.append(waga_elementu)
                print(f"element przeniesiony do paczki {(numer_paczki + 1)} waży: {lista_elementow}kg")
        else:
            if not waga_paczek:
                waga_paczek.append(sum(lista_elementow))
                print("nieprawidowa waga dodanego elementu do paczki, dodawanie paczek zostaje zakończone")
                break
            else:
                if lista_elementow:
                    waga_paczek.append(sum(lista_elementow))
                    print(f"nieprawidowa waga dodanego elementu do paczki {numer_paczki + 1} - dodawanie paczek zostaje zakończone a wszystkie paczki wysłane")
                    break
                else:
                    lista_elementow.clear()
                    print(f"nieprawidowa waga dodanego elementu do paczki {numer_paczki + 1}, paczka {numer_paczki + 1} jest pusta - dodawanie paczek zostaje zakończone a wszystkie paczki wysłane")
                    break

najlzejsza_paczka = min(waga_paczek)
for x in range(len(waga_paczek)):
    puste_kg = 20 - waga_paczek[x]
    puste_kilogramy.append(puste_kg)
    if waga_paczek[x] == najlzejsza_paczka:
        najlzejsze_paczki.append(x + 1)

if sum(waga_paczek) == 0:
    print("brak paczek do wysłania")

else:
    print("PODSUMOWANIE:")
    print(f"1. Wysłano {(len(numery_paczek) + 1)} paczki {wagi_elementów}kg")
    print(f"2. Wysłano {(sum(waga_paczek))}kg")
    print(f"3. Suma pustych kilogramów: {(sum(puste_kilogramy))}kg")
    print(f"4. Najwiecej pustych kg ({(20 - (najlzejsza_paczka))}kg) jest w paczce/paczkach nr: {najlzejsze_paczki}")



