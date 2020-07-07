import numpy as np


class Steering:
    linear = np.asarray([0.0, 0.0])
    angular = 0.0

    def __init__(self, linear, angular):
        self.linear = linear
        self.angular = angular
