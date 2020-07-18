from unittest import TestCase
from ai.graph.graph import Graph


class TestGraph(TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_get_connections_from_node(self):
        self.assertEqual([], self.graph.get_connections_from_node(0))

    def test_get_nodes(self):
        self.assertEqual([], self.graph.get_nodes())
