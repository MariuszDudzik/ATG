def zrob_macierz():
    lista_sasiedztwa = []
    macierz = []

    try:
        while True:
            wiersz = input().strip()
            if wiersz:
                lista = list(map(int, wiersz.split()))
                lista_sasiedztwa.append(lista)
    except EOFError:
        pass

    ilosc = len(lista_sasiedztwa)
    for i in range(ilosc):
        listy_macierzy = []
        for j in range(1, ilosc + 1):
            if j in lista_sasiedztwa[i][1:]:
                listy_macierzy.append(1)
            else:
                listy_macierzy.append(0)
        macierz.append(listy_macierzy)
    return macierz


def mnozenie_macierzy(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Niepoprawne macierze")

    wynik = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                wynik[i][j] += A[i][k] * B[k][j]

    return wynik


def dodaj_macierze(macierzA, macierzB):
    if len(macierzA) != len(macierzB) or len(macierzA[0]) != len(macierzB[0]):
        raise ValueError("Macierze muszą mieć takie same wymiary")

    return [[macierzA[i][j] + macierzB[i][j] for j in range(len(macierzA[0]))] for i in range(len(macierzA))]


def przekatna_macierzy(macierz):
    n = len(macierz)
    diagonalna = [[0] * n for _ in range(n)]
    for i in range(n):
        diagonalna[i][i] = sum(macierz[i])
    return diagonalna


def odejmij_macierze(macierzA, macierzB):
    if len(macierzA) != len(macierzB) or len(macierzA[0]) != len(macierzB[0]):
        raise ValueError("Macierze muszą mieć takie same wymiary")

    return [[macierzA[i][j] - macierzB[i][j] for j in range(len(macierzA[0]))] for i in range(len(macierzA))]


def main():
    macierz = zrob_macierz()
    mnozenie = mnozenie_macierzy(macierz, macierz)
    dodawanie = dodaj_macierze(macierz, mnozenie)
    przekatna = przekatna_macierzy(macierz)
    kwadrat = odejmij_macierze(dodawanie, przekatna)

    lista_sasiedztwa = []
    for i in range(len(kwadrat)):
        lista = [i + 1]  # Numer wierzchołka (1-based index)
        lista.extend(j + 1 for j in range(len(kwadrat[i])) if kwadrat[i][j] > 0)
        lista_sasiedztwa.append(lista)

    for lista in lista_sasiedztwa:
        print(" ".join(map(str, lista)))


if __name__ == "__main__":
    main()