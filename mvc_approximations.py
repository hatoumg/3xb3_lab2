from graph import *
from random import randrange
import matplotlib as plt

#Approximation algorithm implementations

def approx1(G):
    graph = G
    C = {}
    max_deg = math.inf
    for node in range (graph.number_of_nodes):
        if (len(graph[node])) >= max_deg:
            v = i
            C[v] = graph.adjacent_nodes(v)
            graph[v] = []
            if is_vertex_cover(G,C):
                return C

def approx2(G):
    C = {}
    while not is_vertex_cover(G,C):
        v = randrange(G.number_of_nodes)
        if v not in C:
            C[v] = G.adjacent_nodes(v)
    return C

def approx3(G):
    graph = G
    C = {}
    while not is_vertex_cover(G,C):
        u = randrange(graph.number_of_nodes)
        v = graph[u][randrange(len(graph[u]))]
        C[u] = graph.adjacent_nodes=(u)
        C[v] = graph.adjacent_nodes(v)
        graph[u] = []
        graph[v] = []
    return C

#For experiments

def create_random_graph(num, n, m):
    graphs = []
    for i in range(num):
        edges = 0
        graphs.append(Graph(n))
        while edges < m:
            node1 = randrange(n)
            node2 = randrange(n)
            if ((not graphs[i].are_connected(node1, node2)) and node1 != node2):
                graphs[i].add_edge(node1, node2)
                edges += 1
    return graphs
    """ for j in range(num):
        print("graph: ", j)
        for k in range(n):
            print("node: ", k)
            print(graphs[j].adjacent_nodes(k))
 """
def main():
    create_random_graph(1000,8,1)

if __name__ == "__main__":
    main()
