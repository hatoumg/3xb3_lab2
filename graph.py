from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

#Breadth First Search
def BFS2(G, node1, node2):
    l = {}
    l[node1] = node1
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                value = [current_node, node2]
                adding_node = current_node
                while adding_node != node1:
                    value = [l[adding_node]] + value
                    adding_node = l[adding_node]
                return value
            if not marked[node]:
                l[node] = current_node
                Q.append(node)
                marked[node] = True
    return []


#Breadth First Search
def BFS3(G, node1):
    l = {}
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                l[node] = current_node
                Q.append(node)
                marked[node] = True
    return l


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

def DFS2(G, node1, node2):
    S = [node1]
    value = []
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            value.append(current_node)
            for node in G.adj[current_node]:
                if node == node2:
                    value.append(node)
                    return value
                S.append(node)
        elif len(value)!=0:
            value.pop()
    return value

def DFS3(G, node1):
    S = [node1]
    value = {}
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node != node1 and not (node in value):
                    value[node] = current_node
                S.append(node)
    return value

def is_connected(G):
    length = len(G.adj)
    for node in G.adj:
        if len(BFS3(G, node)) != length-1:
            return False
    return True

#Use the methods below to determine minimum Vertex Covers
def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


g = Graph(6)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1, 3)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3, 5)
g.add_edge(3, 4)


print(is_connected(g))