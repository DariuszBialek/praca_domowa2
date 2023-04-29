# Program do zarządzania plikami csv.
# poniżej zakomentowane przykładowe polecenie do wprowadzenia z terminala które...
# ... uruchamia pliku modyfikator_csv.py oraz przekazuje z nowe dane do zmiany:
# python modyfikator_csv in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0

import csv
import sys
import pprint

def read_csv(path):
    with open(path,"r") as f:
        # reader = csv.reader(f)
        data = list(csv.reader(f))
    print(f"zawartość pliku {path}:")
    pprint.pprint(data)
    return data

def writer_csv(path, data):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(data)
    return writer

def modyfy_data(old_data, new_data):
    for i in new_data:
        x, y, value = i.split(',')
        old_data[int(y)][int(x)] = value

print(f"plik wejsciowy: {sys.argv[1]}")
print(f"plik wyjsciowy: {sys.argv[2]}")
print(f"wprowadzane dane: {sys.argv[3:]}")

old_data = read_csv(sys.argv[1])
modyfy_data(old_data, sys.argv[3:])
writer_csv(sys.argv[2], old_data)
new_data = read_csv(sys.argv[2])