import numpy as np

class Edge:
    def __init__(self, origin, destination, weight, next):
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.next = next

class Node:
    def __init__(self):
        self.first = None

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
    
    def addNode(self):
        node = Node()
        self.nodes.append(node)

        return len(self.nodes) - 1

    def addTerminalNodes(self):
        self.foregroundNodeIndex = self.addNode()
        self.backgroundNodeIndex = self.addNode()

        return [self.foregroundNodeIndex, self.backgroundNodeIndex]

    def addEdge(self, origin, destination, weight, revWeight):
        self.edges.append(Edge(origin, destination, weight, self.nodes[origin].first))
        self.nodes[origin].first = len(self.edges)-1

        self.edges.append(Edge(destination, origin, revWeight, self.nodes[destination].first))
        self.nodes[destination].first = len(self.edges)-1

    def toMatrix(self):
        matrix = np.zeros((len(self.nodes), len(self.nodes)))

        for edge in self.edges:
            matrix[edge.origin, edge.destination] = edge.weight

        return matrix