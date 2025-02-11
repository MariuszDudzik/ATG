try:
    macierz = []
    krawedzie = 0
    while True:
        wiersz = input()
        if wiersz == "":
            break
        macierz.append([int(x) for x in wiersz.split()])
except EOFError:
    pass

    for i in range(0, len(macierz)):
        for j in range(0, len(macierz[i])):
            if macierz[i][j] != 0:
                krawedzie += 1
    print("Ilość wierzchołków:",len(macierz))
    print("Ilość krawędzi:",krawedzie // 2)

except (ValueError):
    print("BŁĄD")
