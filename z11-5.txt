import ast
import networkx as nx

slownik = ast.literal_eval(input())
Graf = nx.Graph(slownik)
liscie = [w for w in Graf.nodes if len(list(Graf.neighbors(w))) == 1]

if liscie:
    liscie = sorted(liscie)
    print("Liście:", " ".join(map(str, liscie)))
else:
    print("Liście:")

supporty = []
for l in liscie:
    for neighbor in Graf.neighbors(l):
        if neighbor not in supporty:
            supporty.append(neighbor)

if supporty:
    supporty = sorted(supporty)
    print("Supporty:", " ".join(map(str, supporty)))
else:
    print("Supporty:")