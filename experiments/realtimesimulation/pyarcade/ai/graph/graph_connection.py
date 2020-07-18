class GraphConnection:

    from_node = 0;
    to_node = 0;
    cost = 0;

    def __init__(self, from_node, to_node, cost):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

    def get_cost(self):
        return self.cost

    def get_from_node(self):
        return self.from_node

    def get_to_node(self):
        return self.to_node

