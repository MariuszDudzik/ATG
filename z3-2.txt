lista_sasiedztwa = []
macierz = []
try:
    while True:
        wiersz = input()
        if wiersz == "":
            break
        macierz.append([int(x) for x in wiersz.split()])
except EOFError:
    pass
for i in range(0, len(macierz)):
    x = i+1
    lista = [x]
    for j in range(0, len(macierz[i])):
        if macierz[i][j] == 1:
            y = j + 1
            lista.append(y)
            
    lista_sasiedztwa.append(lista)
    
for i in range(0, len(lista_sasiedztwa)):
        for j in range(0, len(lista_sasiedztwa[i])):
            if j < len(lista_sasiedztwa[i])- 1:
                print(lista_sasiedztwa[i][j], end=' ')
            else:
                print(lista_sasiedztwa[i][j], end='')
        print()
