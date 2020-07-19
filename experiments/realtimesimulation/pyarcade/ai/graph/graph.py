from ai.graph.node import Node
from ai.graph.graph_connection import GraphConnection


class Graph:

    nodes = []
    connections = []

    def __init__(self):
        self.nodes = []

    def get_connections_from_node(self, from_node):
        return self.nodes[from_node].get_connections()

    def get_nodes(self):
        return self.nodes.copy()

    def add_node(self, node):
        self.nodes.append(node)

    def add_connection(self, connection: GraphConnection):
        self.connections.append(connection)
        self.nodes[connection.from_node].add_connection(connection)
        max_node_index = len(self.nodes) - 1
        if connection.from_node > max_node_index or connection.to_node > max_node_index:
            raise IndexError()


# Ref for graphs: https://www.python-course.eu/graphs_python.php
