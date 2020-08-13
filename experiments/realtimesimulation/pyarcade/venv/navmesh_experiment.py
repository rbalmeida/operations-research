import arcade
import heapq
import math
from numpy.random import randint

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
TILE_SIZE = 20

class MyGame(arcade.Window):

    tiles = [(x, y) for x in range(0, SCREEN_WIDTH, TILE_SIZE) for y in range(0, SCREEN_HEIGHT, TILE_SIZE)]
    path_tiles = []
    not_navigable = []

    agent_pos = (0, 0)
    agent_step = 0
    agent_direction = 1

    def setup(self):

        self.not_navigable += [(x, 200) for x in range(100, 600, TILE_SIZE)]
        self.not_navigable += [(x, 600) for x in range(40, 800, TILE_SIZE)]
        self.not_navigable += [(x, 780) for x in range(800, 1200, TILE_SIZE)]
        self.not_navigable += [(800, y) for y in range(780, 900, TILE_SIZE)]
        self.not_navigable += [(x, 900) for x in range(800, 1200, TILE_SIZE)]

        for tile in self.tiles:
            shape = arcade.create_rectangle_outline(tile[0] + TILE_SIZE/2, tile[1] + TILE_SIZE/2, TILE_SIZE, TILE_SIZE, arcade.color.BLUE, 1)
            self.shape_list.append(shape)

        #self.path_tiles = self.pathfind_astar((20, 60), (1000, 800))
        self.path_tiles = self.pathfind_astar(self.tiles[randint(0, len(self.tiles) - 1)], self.tiles[randint(0, len(self.tiles) - 1)])
        # self.path_tiles = self.pathfind_astar(self.tiles[5], self.tiles[4])
        # for tile in self.path_tiles:
        #     shape = arcade.create_rectangle_filled(tile[0] + TILE_SIZE / 2, tile[1] + TILE_SIZE / 2, TILE_SIZE,
        #                                             TILE_SIZE, arcade.color.BLUE, 1)
        #     self.shape_list.append(shape)

        for tile in self.not_navigable:
            shape = arcade.create_rectangle_filled(tile[0] + TILE_SIZE / 2, tile[1] + TILE_SIZE / 2, TILE_SIZE,
                                                   TILE_SIZE, arcade.color.BLACK, 1)
            self.shape_list.append(shape)



    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.shape_list = arcade.ShapeElementList()
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.setup()

    def on_draw(self):
        arcade.start_render()
        for shape in self.shape_list:
            shape.draw()
        if len(self.path_tiles) > self.agent_step:
            self.agent_pos = self.path_tiles[self.agent_step]
        if len(self.path_tiles) > 0:
            arcade.draw_rectangle_filled(self.path_tiles[len(self.path_tiles) - 1][0] + TILE_SIZE/2, self.path_tiles[len(self.path_tiles) - 1][1] + TILE_SIZE/2, TILE_SIZE, TILE_SIZE, arcade.color.GREEN, 1)
        arcade.draw_circle_filled(self.agent_pos[0] + TILE_SIZE/2, self.agent_pos[1] + TILE_SIZE/2, TILE_SIZE/2, arcade.color.RED)



    def update(self, delta_time):
        if self.agent_step < len(self.path_tiles) - 1:
            self.agent_step += 1
        else:
            # print("self.path_tiles")
            # print(self.path_tiles)
            self.path_tiles = self.pathfind_astar(self.path_tiles[len(self.path_tiles) - 1], self.tiles[randint(0, len(self.tiles) - 1)])
            self.agent_step = 0
        #     if self.agent_step > 0:
        #         self.agent_step -= 1
        #     else:
        #         self.agent_direction = 1



    def distance(self, from_tile, to_tile):
        return math.sqrt(math.pow(from_tile[0] - to_tile[0], 2) + math.pow(from_tile[1] - to_tile[1], 2))

    def get_adjacents(self, from_tile):
        adj_tiles = []
        final_adj_tiles = []
        if from_tile[0] > 0:
            if from_tile[1] > 0:
                adj_tiles.append((from_tile[0] - TILE_SIZE, from_tile[1] - TILE_SIZE))
            adj_tiles.append((from_tile[0] - TILE_SIZE, from_tile[1]))
            if from_tile[1] < SCREEN_HEIGHT:
                adj_tiles.append((from_tile[0] - TILE_SIZE, from_tile[1] + TILE_SIZE))

        if from_tile[0] < SCREEN_WIDTH:
            if from_tile[1] > 0:
                adj_tiles.append((from_tile[0] + TILE_SIZE, from_tile[1] - TILE_SIZE))
            adj_tiles.append((from_tile[0] + TILE_SIZE, from_tile[1]))
            if from_tile[1] < SCREEN_HEIGHT:
                adj_tiles.append((from_tile[0] + TILE_SIZE, from_tile[1] + TILE_SIZE))

        if from_tile[1] > 0:
            adj_tiles.append((from_tile[0], from_tile[1] - TILE_SIZE))

        if from_tile[1] < SCREEN_HEIGHT:
            adj_tiles.append((from_tile[0], from_tile[1] + TILE_SIZE))

        for adj_tile in adj_tiles:
            if not adj_tile in self.not_navigable:
                final_adj_tiles.append(adj_tile)

        return final_adj_tiles

    def construct_path(self, came_from, from_tile, to_tile):
        current_tile = to_tile
        path = [current_tile]
        while not current_tile == from_tile:
            current_tile = came_from.pop(current_tile)[0]
            path.append(current_tile)

        return path[::-1]


    def pathfind_astar(self, from_tile, to_tile):

        # TODO refinar: parece que ainda não explorar os melhores caminhos, meio que
        # segue por onde já estava indo
        # ainda precisa de alguns refinamentos

        if from_tile == to_tile:
            path = [from_tile]
            return path[::-1]

        distance_so_far = 0
        best_tiles = []
        closed_tiles = []
        came_from = {}

        heapq.heappush(best_tiles, (distance_so_far, from_tile))

        while len(best_tiles) > 0:
            current_tile = heapq.heappop(best_tiles)[1]
            distance_so_far = distance_so_far + self.distance(current_tile, to_tile)

            if current_tile == to_tile:
                return self.construct_path(came_from, from_tile, to_tile)

            for adj_tile in self.get_adjacents(current_tile):
                if not closed_tiles.__contains__(adj_tile):
                    closed_tiles.append(adj_tile)
                    estimated_distance = distance_so_far + self.distance(adj_tile, to_tile)
                    heapq.heappush(best_tiles, (estimated_distance, adj_tile))
                    came_from[adj_tile] = (current_tile, estimated_distance)
                # else:
                #     prev_distance = came_from.get(adj_tile)[1]
                #     estimated_distance = distance_so_far + self.distance(adj_tile, to_tile)
                #     if estimated_distance < prev_distance:
                #         came_from.pop(adj_tile)
                #         heapq.heappush(best_tiles, (estimated_distance, adj_tile))
                #         came_from[adj_tile] = (current_tile, estimated_distance)

        return []


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()

main()

# ref for fast draw
# https://arcade.academy/examples/shapes_buffered.html