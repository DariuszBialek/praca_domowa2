# Program do zarządzania plikami csv.
# poniżej zakomentowane przykładowe polecenie do wprowadzenia z terminala które...
# ... uruchamia pliku modyfikator_csv.py oraz przekazuje nowe dane do zmiany:
# python modyfikator_csv.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
# python modyfikator_csv.py in.csv out.csv 0/0/gitara 3/1/kubek 1/2/17 3/3/0
###############################################
import csv
import sys
import pprint
import os

def read_csv(path):
    with open(path, "r") as f:
        data = list(csv.reader(f))
    print(f"Zawartość pliku {path}:")
    pprint.pprint(data)
    return data

def write_csv(path, data):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(data)

# znaki rozdzielajace "," "/"
def modify_data(old_data, new_data):
    for i in new_data:
        if "," in i:
            x, y, value = i.split(',')
        else:
            x, y, value = i.split('/')
        old_data[int(y)][int(x)] = value

# spr. ilośc parametrów - min pliki i 1 zmiana danych, max zmiana wszystkich parametrów)
if len(sys.argv) < 4 or len(sys.argv) > 7:
    print("Nieprawidłowa liczba parametrów.")
    print("Użycie: python modyfikator_csv.py <plik_wejściowy> <plik_wyjściowy> <zmiany>")
    sys.exit(1)

# spr. nazwę pliku wej.
input_file = sys.argv[1]
if not os.path.isfile(input_file):
    print(f"Podany plik wejściowy '{input_file}' nie istnieje.")
    sys.exit(1)

print(f"Plik wejściowy: {input_file}")
print(f"Plik wyjściowy: {sys.argv[2]}")
print(f"Wprowadzane dane: {sys.argv[3:]}")

old_data = read_csv(input_file)
modify_data(old_data, sys.argv[3:])
write_csv(sys.argv[2], old_data)
new_data = read_csv(sys.argv[2])

