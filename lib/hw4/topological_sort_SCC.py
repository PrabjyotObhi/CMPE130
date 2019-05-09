from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v)

    def sort(self, v, marked, stack):
        marked[v] = True
        for i in self.graph[v]:
            if marked[i] is False:
                self.sort(i, marked, stack)
        stack.insert(0, v)

    def topological_Sort(self):
        marked = self.V * [False]
        stack = []
        for i in range(self.V):
            if marked[i] is False:
                self.sort(i, marked, stack)
        print(stack)
        return 1

    def DFS(self, v, visited):
        visited[v] = True
        print(v, )
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i, visited)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    def Transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def SCC(self):

        stack = []
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        gr = self.Transpose()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)

        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFS(i, visited)
                print(" ")