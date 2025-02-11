import networkx as nx
import numpy as np

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

def oblicz_macierz_odleglosci(macierz_sasiedztwa):
    G = nx.Graph()
    for i, wiersz in enumerate(macierz_sasiedztwa):
        for j, wartosc in enumerate(wiersz):
            if wartosc == 1:
                G.add_edge(i, j)
 
    odleglosci = nx.single_source_shortest_path_length(G, 0)
    maks_wierzcholek = max(odleglosci.keys())
    macierz_odleglosci = [odleglosci.get(i, float('inf')) for i in range(maks_wierzcholek + 1)]
    return macierz_odleglosci


def main():
    macierz_sasiedztwa = wczytaj_macierz_sasiedztwa()
    macierz_odleglosci = oblicz_macierz_odleglosci(macierz_sasiedztwa)
    print(" ".join(map(str, macierz_odleglosci)))

if __name__ == "__main__":
    main()