
lista_sasiedztwa = []
macierz = []

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
    listy_macierzy = []
    for j in range(1, ilosc + 1):
        if j in lista_sasiedztwa[i][1:]:
             listy_macierzy.append(1)
        else:
             listy_macierzy.append(0)
    macierz.append(listy_macierzy)
                   
    
for i in range(0, len(macierz)):
        for j in range(0, len(macierz[i])):
            if j < len(macierz[i])- 1:
                print(macierz[i][j], end=' ')
            else:
                print(macierz[i][j], end='')
        print()
    