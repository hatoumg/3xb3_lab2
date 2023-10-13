from graph.py import *
from random import randrange
import matplotlib as plt

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
