from itertools import combinations
from graph import *

def is_ind_set(G: Graph, ind_set):

    if len(ind_set) == 1:
        return True

    for u, v in combinations(ind_set, 2):
        if G.are_connected(u, v):
            return False

    return True

def MIS(G:Graph):
    max_ind_size = 0
    max_ind_set = set()
    n = G.number_of_nodes() 

    for size in range (1, n + 1):
        for nodes in combinations(G.get_node_list(), size):
            #print(nodes)
            if is_ind_set(G, nodes) and len(nodes) > max_ind_size:
                max_ind_size = size
                max_ind_set = nodes  

    return max_ind_set

g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)

print(MIS(g))

