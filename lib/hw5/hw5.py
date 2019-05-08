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


def BFS(self, s, t, parent):

    # Mark all the vertices as not visited
    visited = [False] * (self.ROW)

    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    # Standard BFS Loop
    while queue:

        # Dequeue a vertex from queue and print it
        u = queue.pop(0)

        # Get all adjacent vertices of the dequeued vertex u
        # If a adjacent has not been visited, then mark it
        # visited and enqueue it
        for ind, val in enumerate(self.graph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

                # If we reached sink in BFS starting from source, then return
    # true, else false
    return True if visited[t] else False

# Returns tne maximum flow from s to t in the given graph
def FordFulkerson(self, source, sink):
    # This array is filled by BFS and to store path
    parent = [-1] * (self.ROW)

    max_flow = 0  # There is no flow initially

    # Augment the flow while there is path from source to sink
    while self.BFS(source, sink, parent):

        # Find minimum residual capacity of the edges along the
        # path filled by BFS. Or we can say find the maximum flow
        # through the path found.
        path_flow = float("Inf")
        s = sink
        while (s != source):
            path_flow = min(path_flow, self.graph[parent[s]][s])
            s = parent[s]

            # Add path flow to overall flow
        max_flow += path_flow

        # update residual capacities of the edges and reverse edges
        # along the path
        v = sink
        while (v != source):
            u = parent[v]
            self.graph[u][v] -= path_flow
            self.graph[v][u] += path_flow
            v = parent[v]

    return max_flow