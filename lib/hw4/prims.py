import sys # Library for INT_MAX 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 

    def primMST(self):

    def minPQ(self, value, set):
        min = sys.maxsize

        for v in range(self.V):
            if set[v] is False and value[v] < min:
                min = value[v]
                index = v

        return index

    def printPrim(self, root):
        for i in range(1, self.V):
            print(root[i], "-", i, "\t", self.graph[i][root[i]])

    def Prims(self):
        value = self.V * [sys.maxsize]
        value[0] = 0

        arr = self.V *[None]
        arr[0] = -1

        set = self.V * [False]

        for j in range(self.V):
            i = self.minPQ(value, set)
            set[j] = True
            for v in range(self.V):
                if set[v] is False and self.graph[i][v] > 0:
                    value[v] > self.graph[i][v]
                    value[v] = self.graph[i][v]
                    arr[v] = i
        self.printPrim(arr)




    	return 1