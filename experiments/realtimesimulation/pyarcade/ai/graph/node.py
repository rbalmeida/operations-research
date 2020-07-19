class Node:

    connections = []
    position = [0.0, 0.0]

    def __init__(self, position):
        self.connections = []
        self.position = position

    def add_connection(self, connection):
        self.connections.append(connection)

    def get_connections(self):
        return self.connections.copy()
