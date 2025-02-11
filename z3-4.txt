lista_sasiedztwa = []
stopnie_wejsciowe = []
stopnie_wyjsciowe = []

try:
    while True:
        wiersz = input()
        if wiersz.strip() != "":
            lista = list(map(int, wiersz.split()))
            lista_sasiedztwa.append(lista)
except EOFError:
    pass

ilosc = len(lista_sasiedztwa)
for i in range(0, ilosc):
    stopnie_wyjsciowe.append(len(lista_sasiedztwa[i]) -1)
    x = i + 1
    zlicz = -1
    for j in range(0, ilosc):
        for k in range(0, len(lista_sasiedztwa[j])):
            if x == lista_sasiedztwa[j][k]:
                zlicz += 1
    stopnie_wejsciowe.append(zlicz)
 
print("Stopnie wejściowe:", ' '.join(map(str, stopnie_wejsciowe)))
print("Stopnie wyjściowe:", ' '.join(map(str, stopnie_wyjsciowe)))
