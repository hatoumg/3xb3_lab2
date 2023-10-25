from random import *
from graph import *
import matplotlib.pyplot as plot

def create_random_graph(i, j):
    edges = 0
    graphs= Graph(i)
    while edges < j:
        node1 = randrange(i)
        node2 = randrange(i)
        if ((not graphs.are_connected(node1, node2)) and node1 != node2):
            graphs.add_edge(node1, node2)
            edges += 1
    return graphs

def probability(min=0, inc=1, n=100, e=200, r=1000, f=has_cycle):
    prob = {}
    for i in range(min, e, inc):
        sum = 0
        for _ in range(r):
            g = create_random_graph(n, i)
            if f(g):
                sum += 1
        prob[i] = (1.0*sum/r)
    return prob


def main():
    v, p = [], []
    t = probability(f=has_cycle)
    for key in t:
        v.append(key)
        p.append(t[key])
    plot.plot(v, p)
    plot.xlabel("Number of Edges")
    plot.ylabel("Cycle Probability")
    plot.show()

if __name__ == "__main__":
    main()