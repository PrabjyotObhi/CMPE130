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

    def SCC(self):    # strongly connected componentssx

    # return 1
