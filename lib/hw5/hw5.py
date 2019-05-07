class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(to_node, length)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge

class Node:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, to_node, length):
        self.to_node = to_node
        self.length = length


def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node,"t",dist[node])

def minDistance(self, dist, sptSet):
    # Initilaize minimum distance for next node
    min = sys.maxint

    # Search not nearest vertex not in the
    # shortest path tree
    for v in range(self.V):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index


def dijkstra(self, src):
    dist = [sys.maxint] * self.V
    dist[src] = 0
    sptSet = [False] * self.V

    for cout in range(self.V):

        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = self.minDistance(dist, sptSet)

        # Put the minimum distance vertex in the
        # shotest path tree
        sptSet[u] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shotest path tree
        for v in range(self.V):
            if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.Graph[u][v]:
                dist[v] = dist[u] + self.Graph[u][v]


self.printSolution(dist)

def BellmanFord(graph, source):

    return 1

def Ford_fullerskon(graph, source, sink):    # you can implement Bfs or dfs to get the path from source(start node) to sink(end node)

    return 1 