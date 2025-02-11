def wczytaj():
    wejscie = []
    try:
        while True:
            wiersz = input()
            if wiersz.strip() != "":
                lista = list(map(int, wiersz.split()))
                wejscie.append(lista)
    except EOFError:
        pass
    return wejscie


def zrob_wk(lista_sasiedztwa):
    lista_wk = []
    for i in range(len(lista_sasiedztwa)):
        for j in range(1, len(lista_sasiedztwa[i])):
            a = lista_sasiedztwa[i][0]
            b = lista_sasiedztwa[i][j]
            w = (a, b)
            znacznik = False # nieskierowany
            if a in lista_sasiedztwa[b-1]:
                znacznik = True
            if znacznik == True:
                w = (a, b, "n")
                w1 = (b, a, "n")
                if w not in lista_wk and w1 not in lista_wk:
                    lista_wk.append(w)
            else:
                w = (a, b, "s")
                if w not in lista_wk:
                    lista_wk.append(w)
    return lista_wk


def lista_krawedziowa(lista_wk):
    lista_kra = []
    for i in range(len(lista_wk)):
        temp = []
        temp.append(lista_wk[i])
        if lista_wk[i][2] == "n":
            for j in range(len(lista_wk)):
                if i != j:
                    a = lista_wk[i][0]
                    b = lista_wk[i][1]
                    if a in lista_wk[j] or b in lista_wk[j]:
                        temp.append(lista_wk[j])
        else:
            for j in range(len(lista_wk)):
                if i != j:
                    b = lista_wk[i][1]
                    if b == lista_wk[j][0] and lista_wk[j]:
                        temp.append(lista_wk[j])
        lista_kra.append(temp)
    return lista_kra


def wyswietl_lista_kra(lista_kra):
    for krawedzie in lista_kra:
        print(" ".join(f"({krawedz[0]}, {krawedz[1]})" for krawedz in krawedzie))

def main():
    lista_sasiedztwa = wczytaj()
    lista_wk = zrob_wk(lista_sasiedztwa)
    lista_kra = lista_krawedziowa(lista_wk)
    wyswietl_lista_kra(lista_kra)
   # print(lista_wk)

if __name__ == "__main__":
    main()