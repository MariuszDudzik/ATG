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
    G = nx.Graph()
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] != 0:
                G.add_edge(i, j, waga=macierz[i][j])
    return G

def main():
    macierz = wczytaj_macierz_sasiedztwa()
    G = tworz_graf(macierz)

    if not nx.is_connected(G):
        print("Graf nie jest spójny")
    else:
        mst = nx.minimum_spanning_tree(G, weight='waga')
        waga_mst = int(mst.size(weight='waga'))
        print(waga_mst)

if __name__ == "__main__":
    main()