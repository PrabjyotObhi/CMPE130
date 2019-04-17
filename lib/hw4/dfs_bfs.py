from collections import defaultdict 

class Graph:
	def __init__(self): 
		self.graph = defaultdict(list) 

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def dfs(self, v, visited):
		visited[v] = True
		print(v)
		for i in self.Graph(V):
			if visited[i] == False:
				self.dfs(self, i, visited)

	def DFS(self, v):
		visited = [False]*(len(self.Graph))
		self.dfs(v, visited)
		return 1

	def bfs(self, v):
		visited = [False]*(len(self.Graph))
		queue = []
		queue.append(v)
		visited[v] = True

		while queue:
			v = queue.pop(0)
			print(v, end=" ")
			for i in self.Graph[v]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True





		return 1 
