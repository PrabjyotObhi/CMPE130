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

        # check if input node is already in graph
        if node in self.nodeList:
            print("Node already in graph, unable to add")
            return

        # add node to list, add node to dictionaries
        self.nodeList.add(node)
        self.parents[node] = dict()
        self.children[node] = dict()

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
        """checks if a connection exists between two given nodes in your graph, returns boolean"""

        # check if tail or head exist | If they do not exist, return false
        # return true if last exists in child dictionary
        # if it does not exist in dictionary, it has not been added yet
        return first in self.nodeList and last in self.children[first]

    def remove_edge(self, first, last):
        """removes edges between two given vertices in your graph"""
        # use del dict method to delete from dictionary
        # decrement edgeNum
        del self.parents[last][first]
        del self.children[first][last]
        self.edgeNum -= 1

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

