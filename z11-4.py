import networkx as nx

def wczytaj_macierz_sasiedztwa():
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
    return macierz

def tworz_graf(macierz):
    G = nx.DiGraph()
    for i in range(len(macierz)):
        G.add_node(i)

    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] == 1:
                G.add_edge(i, j)
    return G


def main():
    macierz_sasiedztwa = wczytaj_macierz_sasiedztwa()
    graf = tworz_graf(macierz_sasiedztwa)
    ujscia = [node for node in graf.nodes if graf.out_degree(node) == 0]
    zrodla = [node for node in graf.nodes if graf.in_degree(node) == 0]
    print("Ilość ujść:", len(ujscia))
    print("Ilość źródeł:", len(zrodla))

if __name__ == "__main__":
    main()