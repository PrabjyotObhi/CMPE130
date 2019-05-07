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


def BellmanFord(self, src):
    # Step 1: Initialize distances from src to all other vertices
    # as INFINITE
    dist = [float("Inf")] * self.V
    dist[src] = 0

    # Step 2: Relax all edges |V| - 1 times. A simple shortest
    # path from src to any other vertex can have at-most |V| - 1
    # edges
    for i in range(self.V - 1):
        # Update dist value and parent index of the adjacent vertices of
        # the picked vertex. Consider only those vertices which are still in
        # queue
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

                # Step 3: check for negative-weight cycles.  The above step
    # guarantees shortest distances if graph doesn't contain
    # negative weight cycle.  If we get a shorter path, then there
    # is a cycle.

    for u, v, w in self.graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print
            "Graph contains negative weight cycle"
            return

    # print all distance
    self.printArr(dist)

def Ford_fullerskon(graph, source, sink):    # you can implement Bfs or dfs to get the path from source(start node) to sink(end node)

    return 1 