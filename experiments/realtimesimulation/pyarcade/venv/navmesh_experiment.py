import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Graph:
    # nodes = [(1, 1), (20, 40), (30, 20), (50, 50), (100, 120)]
    nodes = [(x, y) for x in range(40, SCREEN_WIDTH, 50) for y in range(40, SCREEN_HEIGHT, 50)]

class Ball:


    def __init__(self, position_x, position_y, change_x, change_y, radius, color):



        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):

        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):

    graph = Graph()

    def setup(self):

        for node in self.graph.nodes:
            shape = arcade.create_ellipse(node[0], node[1], 10, 10, arcade.color.BLUE)
            self.shape_list.append(shape)

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.shape_list = arcade.ShapeElementList()
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.ball = Ball(50, 50, 3, 3, 15, arcade.color.RED)
        self.setup()

    def on_draw(self):
        arcade.start_render()
        for shape in self.shape_list:
            shape.draw()
        self.ball.draw()


    def update(self, delta_time):
        self.ball.update()


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()

main()

# ref for fast draw
# https://arcade.academy/examples/shapes_buffered.html