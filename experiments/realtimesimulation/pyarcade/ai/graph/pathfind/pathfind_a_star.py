from collections import namedtuple
from collections import OrderedDict
from operator import itemgetter
from typing import List

from ai.graph.graph import Graph
from ai.graph.node import Node
from ai.graph.graph_connection import GraphConnection
from math import sqrt, pow


class PathfindAStar:

    def find_path(self, graph: Graph, start: Node, end: Node):

        NodeRecord = namedtuple('NodeRecord', ['node', 'connection', 'cost_so_far', 'estimated_total_cost'])
        current: NodeRecord
        connections: List[GraphConnection]

        start_record = NodeRecord()
        start_record.node = start
        start_record.connection = None
        start_record.cost_so_far = 0
        start_record.estimated_total_cost = self.estimate(start, end)

        open = OrderedDict(int, NodeRecord)
        open.add(start_record.estimated_total_cost, start_record)
        closed = OrderedDict(int, NodeRecord)

        while len(open) > 0:
            current = open.pop()

            if current.node == end:
                break

            connections = current.node.get_connections()

            for connection in connections:
                end_node = connection.to_node
                end_node_cost = current.cost_so_far + connection.get_cost()

                if closed.__contains__(end_node):
                    end_node_record = closed.

                if end_node_record.cost_so_far <= end_node_cost
                    continue





    def estimate(self, from_node:Node, to_node:Node):
        return sqrt( pow(from_node.position[0] - to_node.position[0], 2), pow(from_node.position[1] - to_node.position[1], 2))