from graph import *
from random import *
from copy import deepcopy
import random
import matplotlib.pyplot as plt
import math

#Approximation algorithm implementations

def approx1(G):
    graph = deepcopy(G)
    C = set()
    while True:
        max_deg = 0
        for node in range(graph.number_of_nodes()):
            if (len(graph.adjacent_nodes(node))) > max_deg:
                v = node
                max_deg = len(graph.adjacent_nodes(node))
        C.add(v)
        for incident_node in (graph.adjacent_nodes(v)):
            graph.adjacent_nodes(v).remove(incident_node)
            graph.adjacent_nodes(incident_node).remove(v)
        if is_vertex_cover(G,C):
            return C

def approx2(G):
    C = set()
    while not is_vertex_cover(G,C):
        while True: 
            v = random.choice(list(G.adj.keys()))
            if G.adjacent_nodes(v) != []:
                break
        if v not in C:
            C.add(v)
    return C

def approx3(G):
    graph = deepcopy(G)
    C = set()
    while not is_vertex_cover(G,C):
        while True:
            u = random.choice(list(graph.adj.keys()))
            if graph.adjacent_nodes(u) != []:
                v = random.choice(list(graph.adjacent_nodes(u)))
                break
        C.add(u)
        C.add(v)
        del graph.adj[u]
        if v in graph.adj:
            del graph.adj[v]
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

def experiment1():
    graph_sizes = []
    a1_performance = []
    a2_performance = []
    a3_performance = []
    for i in range(1,30,5):
        graph_sizes.append(i)
        graphs = create_random_graph(1000,8,i)
        sum_mvc = 0
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for graph in graphs:
            mvc = MVC(graph)
            sum_mvc += len(mvc)
            a1 = approx1(graph)
            sum1 += len(a1)
            a2 = approx2(graph)
            sum2 += len(a2)
            a3 = approx3(graph)
            sum3 += len(a3)
        a1_performance.append(sum1/sum_mvc)
        a2_performance.append(sum2/sum_mvc)
        a3_performance.append(sum3/sum_mvc)
    return graph_sizes, a1_performance, a2_performance, a3_performance

def experiment2():
    graph_sizes = []
    a1_performance = []
    a2_performance = []
    a3_performance = []
    for i in range(2,20):
        print(i)
        graph_sizes.append(i)
        graphs = create_random_graph(1000,i,i-1)
        sum_mvc = 0
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for graph in graphs:
            mvc = MVC(graph)
            sum_mvc += len(mvc)
            a1 = approx1(graph)
            sum1 += len(a1)
            a2 = approx2(graph)
            sum2 += len(a2)
            a3 = approx3(graph)
            sum3 += len(a3)
        a1_performance.append(sum1/sum_mvc)
        a2_performance.append(sum2/sum_mvc)
        a3_performance.append(sum3/sum_mvc)
    return graph_sizes, a1_performance, a2_performance, a3_performance

def experiment3():
    graph_sizes = []
    a1_performance = []
    for i in range(1,11):
        print(i)
        graph_sizes.append(i)
        graphs = create_random_graph(10000,5,i)
        sum_mvc = 0
        sum1 = 0
        for graph in graphs:
            mvc = MVC(graph)
            sum_mvc += len(mvc)
            a1 = approx1(graph)
            sum1 += len(a1)
        a1_performance.append(sum1/sum_mvc)
    return graph_sizes, a1_performance

def main():
    #x, a1_performance, a2_performance, a3_performance = experiment1()
    #x, a1_performance, a2_performance, a3_performance = experiment2()
    x, a1_performance = experiment3()

    plt.plot(x, a1_performance)
    #plt.plot(x, a2_performance)
    #plt.plot(x, a3_performance)
    #plt.legend(["approx1", "approx2", "approx3"])
    plt.xlabel("Number of edges")
    plt.ylabel("Performance (approx# sum / mvc sum)")
    plt.show()

if __name__ == "__main__":
    main()