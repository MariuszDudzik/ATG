import ast
import networkx as nx

graf = {}
with open("lista.txt", "r") as file:
    lista_sasiedztwa = file.read()
    
for line in lista_sasiedztwa.splitlines():
    czesc = line.split()
    if czesc:
        node = czesc[0]
        sasiedzi = czesc[1:]
        graf[node] = sasiedzi
G = nx.Graph(graf)
stopien2 = [node for node, stopien in G.degree() if stopien == 2]
stopien2.sort()
print("Wierzchołki stopnia 2:", " ".join(map(str, stopien2)))