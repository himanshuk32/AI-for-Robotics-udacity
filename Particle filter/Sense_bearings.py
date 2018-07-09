# --------------
# USER INSTRUCTIONS
#
# Write a function in the class robot called sense()
# that takes self as input
# and returns a list, Z, of the four bearings* to the 4
# different landmarks. you will have to use the robot's
# x and y position, as well as its orientation, to
# compute this.
from math import *
import random

#
# the "world" has 4 landmarks.
# the robot's initial coordinates are somewhere in the square
# represented by the landmarks.
#
# NOTE: Landmark coordinates are given in (y, x) form and NOT
# in the traditional (x, y) format!

landmarks = [[0.0, 100.0], [0.0, 0.0], [100.0, 0.0], [100.0, 100.0]]  # position of 4 landmarks in (y, x) form.
world_size = 100.0  # world is NOT cyclic. Robot is allowed to travel "out of bounds"


# ------------------------------------------------
#
# this is the robot class
#

class robot:


    def __init__(self, length=10.0):
        self.x = random.random() * world_size  # initial x position
        self.y = random.random() * world_size  # initial y position
        self.orientation = random.random() * 2.0 * pi  # initial orientation
        self.length = length  # length of robot
        self.bearing_noise = 0.0  # initialize bearing noise to zero
        self.steering_noise = 0.0  # initialize steering noise to zero
        self.distance_noise = 0.0  # initialize distance noise to zero

    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y),
                                                str(self.orientation))

    def set(self, new_x, new_y, new_orientation):
        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise (ValueError, 'Orientation must be in [0..2pi]')
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)


    def set_noise(self, new_b_noise, new_s_noise, new_d_noise):
        self.bearing_noise = float(new_b_noise)
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)


    def sense(self):  # do not change the name of this function
        Z = []
        add_noise = 0
        for i in range(len(landmarks)):
            bearing = atan2(landmarks[i][0] - self.y, landmarks[i][1] - self.x) - self.orientation
            if add_noise:
                bearing = bearing + random.gauss(0.,self.bearing_noise)
            bearing = bearing % (2 * pi)
            Z.append(bearing)
        return Z

length = 20.
bearing_noise = 0.0
steering_noise = 0.0
distance_noise = 0.0

myrobot = robot(length)
myrobot.set(30.0, 20.0, 0.0)
myrobot.set_noise(bearing_noise, steering_noise, distance_noise)

print ('Robot:        ', myrobot)
print ('Measurements: ', myrobot.sense())
