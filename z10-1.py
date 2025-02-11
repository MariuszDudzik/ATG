def wczytaj():
    wejscie =[]
    try:
        while True:
            wiersz = input()
            if wiersz.strip() != "":
                lista = list(map(int, wiersz.split()))
                wejscie.append(lista)
        
    except EOFError:
        pass
    return wejscie

def dopelnienie(lista_sasiedztwa):
    dopelnienie = []
    for i in range(len(lista_sasiedztwa)):
        temp = []
        temp.append(i+1)
        for j in range (len(lista_sasiedztwa)):
            if j + 1 not in lista_sasiedztwa[i]:
                temp.append(j+1)
        dopelnienie.append(temp)
    return dopelnienie

def wypisz(dop):
    for i in range(len(dop)):
        print(' '.join(map(str, dop[i])))

                           
def main():
    lista_sasiedztwa = wczytaj()
    dop = dopelnienie(lista_sasiedztwa)
    wypisz(dop)
             
if __name__ == "__main__":
    main()