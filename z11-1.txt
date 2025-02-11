import ast
import networkx as nx

slownik = ast.literal_eval(input())
Graf = nx.Graph(slownik)
c_Graf = nx.complement(Graf)
A = nx.adjacency_matrix(c_Graf)
print(A.todense())
k_Graf = nx.line_graph(Graf)
k = nx.adjacency_matrix(k_Graf).todense()
print(k)