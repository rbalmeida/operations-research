from ai.kinematic.steering import Steering
import numpy as np


class Kinematic:
    position = np.asarray([0.0, 0.0])
    orientation = 0.0
    velocity = np.asarray([0.0, 0.0])
    rotation = 0.0
    steering: Steering

    def __init__(self, position, orientation, velocity, rotation):
        self.position = position
        self.orientation = orientation
        self.velocity = velocity
        self.rotation = rotation

    def update_steering(self, steering: Steering):
        self.steering = steering

    def update(self, delta_time):
        self.position += self.velocity * delta_time + \
                         self.steering.linear * delta_time
        self.orientation += self.rotation * delta_time + \
                            self.steering.angular * delta_time

        self.velocity += self.steering.linear * delta_time
        self.rotation += self.steering.angular * delta_time
