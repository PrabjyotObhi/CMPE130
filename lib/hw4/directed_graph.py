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

    def remove(self, node):
        """ Remove all references to node """
        print("Hi, does this work")

        for n, cxns in self.Digraph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self.Digraph[node]
        except KeyError:
            pass
        
        return 1

    def contains(self, node):
        """checks if your graph contains a given value"""

        return 1

