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

def oblicz_srednice(G):
        najkrotsza = dict(nx.all_pairs_dijkstra_path_length(G, weight="waga"))       
        srednica = max(max(d.values()) for d in najkrotsza.values())
        return srednica
    
def main():
    macierz = wczytaj_macierz_sasiedztwa()
    G = tworz_graf(macierz)
    srednica = oblicz_srednice(G)
    print(srednica)
  
if __name__ == "__main__":
    main()