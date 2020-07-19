from unittest import TestCase
from ai.graph.graph import Graph
from ai.graph.node import Node
from ai.graph.graph_connection import GraphConnection


class TestGraph(TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_get_connections_from_node(self):
        graph = Graph()
        graph.add_node(Node([0.0, 0.0]))
        self.assertEqual([], graph.get_connections_from_node(0))

    def test_get_nodes_empty(self):
        graph = Graph()
        self.assertEqual([], graph.get_nodes())

    def test_add_nodes(self):
        graph = Graph()
        graph.add_node(Node([0.0, 0.0]))
        graph.add_node(Node([0.0, 0.5]))
        graph.add_node(Node([1.0, 5.0]))
        self.assertEqual(3, len(graph.get_nodes()))

    def test_add_connections(self):
        graph = Graph()
        graph.add_node(Node([0.0, 0.0]))
        graph.add_node(Node([0.0, 0.5]))
        graph.add_node(Node([1.0, 5.0]))
        con1 = GraphConnection(0, 1, 10)
        graph.add_connection(con1)
        self.assertEqual(1, len(graph.get_connections_from_node(0)))
        self.assertEqual(0, len(graph.get_connections_from_node(1)))
        self.assertEqual(0, len(graph.get_connections_from_node(2)))

    def test_print_connections(self):
        graph = Graph()
        graph.add_node(Node([0.0, 0.0]))
        graph.add_node(Node([0.0, 0.5]))
        graph.add_node(Node([1.0, 5.0]))
        con1 = GraphConnection(0, 1, 10)
        graph.add_connection(con1)
        con1 = GraphConnection(0, 2, 30)
        graph.add_connection(con1)
        self.assertEqual(2, len(graph.get_connections_from_node(0)))
        self.assertEqual(0, len(graph.get_connections_from_node(1)))
        self.assertEqual(0, len(graph.get_connections_from_node(2)))
        for con in graph.get_connections_from_node(0):
            print("From {} to {} cost {}".format(con.get_from_node(), con.get_to_node(), con.get_cost()))

    def test_invalid_node_for_connection(self):
        graph = Graph()
        graph.add_node(Node([0.0, 0.0]))
        con1 = GraphConnection(0, 1, 10)
        with self.assertRaises(IndexError) as context:
            graph.add_connection(con1)
            self.assertTrue('IndexError' in str(context.exception))

