class Digraph:
    """This class implements a directed graph with nodes represented by integers. """

    def __init__(self):
        """Initializes this digraph."""
        self.edgeNum = 0  # number of edges
        self.nodeList = set()  # graph nodes
        self.parents = dict()  # parents held in dict
        self.children = dict()  # children held in dict

    def add_node(self, node):
        """adds vertices to your graph"""

        return 1
    def add_edge(self, first, last, weight):
        """creates edge from 'first' to 'last' with assigned 'weight'"""

        # first check that first or last are not already nodes
        # if they do not exist, create them as new nodes
        if first not in self.nodeList:
            self.add_node(first)

        if last not in self.nodeList:
            self.add_node(last)

        # update dictionaries with correct weight and direction
        self.parents[last][first] = weight
        self.children[first][last] = weight

        # Increment edgeNum
        self.edgeNum += 1
        return 1

    def has_edge(self, first, last):   
        """checks if a connection exists between two given nodes in your graph"""
        

        return 1

    def remove_edge(self, last, first):
        """removes edges between two given vertices in your graph"""
        
        return 1

    def remove_node(self, node):
        """removes nodes from your graph along with any vertices they induce"""
        # check if input node is not in graph
        if node not in self.nodeList:
            print("Node not in graph, unable to delete")
            return

        # decrement edgeNum by the number of edges affected by deleting node
        self.edgeNum -= len(self.parents[node]) + len(self.children[node])

        # Delete parent link
        for link1 in self.parents[node]:
            del self.children[link1][node]

        # Delete Child link
        for link2 in self.children[node]:
            del self.parents[link2][node]

        # Delete node from dictionaries
        del self.parents[node]
        del self.children[node]
        self.nodeList.remove(node)

    def contains(self, node):
        """checks if your graph contains a given value"""
        # returns true if node is found
        # returns false if not found
        return node in self.nodeList

