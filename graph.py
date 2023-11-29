# graph.py
class Graph:
    """
    Represents a graph data structure.

    Attributes:
        graph (dict): A dictionary representing the graph.
    """

    def __init__(self):
        """Initializes an empty graph."""
        self.graph = {}

    def add_edge(self, node1, node2):
        """
        Adds an edge to the graph.

        Args:
            node1: The first node in the edge.
            node2: The second node in the edge.
        """
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

    def display_graph(self):
        """Displays the graph."""
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")
