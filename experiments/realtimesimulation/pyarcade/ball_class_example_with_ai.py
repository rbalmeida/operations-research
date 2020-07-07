import arcade
import numpy as np
from ai.kinematic.kinematic import Kinematic
from ai.kinematic.steering import Steering

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    kinematic: Kinematic
    steering: Steering

    def __init__(self, kinematic, steering, radius, color):
        self.kinematic = kinematic
        self.steering = steering
        self.radius = radius
        self.color = color

    def draw(self):

        arcade.draw_circle_filled(self.kinematic.position[0], self.kinematic.position[1], self.radius, self.color)

    def update(self, delta_time):
        self.kinematic.update(delta_time)

        if self.kinematic.position[0] < self.radius:
            self.steering.linear[0] *= -1
            self.kinematic.velocity[0] *= -1
            # self.kinematic.update_steering(self.steering)

        if self.kinematic.position[0] > SCREEN_WIDTH - self.radius:
            self.steering.linear[0] *= -1
            self.kinematic.velocity[0] *= -1
            # self.kinematic.update_steering(self.steering)

        if self.kinematic.position[1] < self.radius:
            self.steering.linear[1] *= -1
            self.kinematic.velocity[1] *= -1
            # self.kinematic.update_steering(self.steering)

        if self.kinematic.position[1] > SCREEN_HEIGHT - self.radius:
            self.steering.linear[1] *= -1
            self.kinematic.velocity[1] *= -1
            # self.kinematic.update_steering(self.steering)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        steering = Steering(np.asarray([-10.0, -5.0]), 0.0)
        kinematic = Kinematic(np.asarray([100.0, 100.0]), 0.0, np.asarray([30.0, 60.0]), 0.0)
        kinematic.update_steering(steering)
        self.ball = Ball(kinematic, steering, 15.0, arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update(delta_time)


def main():
    window = MyGame(640, 480, "AI Steering Example")

    arcade.run()

main()