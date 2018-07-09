# -----------------
# USER INSTRUCTIONS
#
# A function in the class robot called move()
#
# that takes self and a motion vector (this
# motion vector contains a steering* angle and a
# distance) as input and returns an instance of the class
# robot with the appropriate x, y, and orientation
# for the given motion.
#
# *steering is defined in the video
# which accompanies this problem.
#
# For now, please do NOT add noise to your move function.
#
# Please do not modify anything except where indicated
# below.
#
# There are test cases which you are free to use at the
# bottom. If you uncomment them for testing, make sure you
# re-comment them before you submit.

from math import *
import random

landmarks = [[0.0, 100.0], [0.0, 0.0], [100.0, 0.0], [100.0, 100.0]]  # position of 4 landmarks
world_size = 100.0  # world is NOT cyclic. Robot is allowed to travel "out of bounds"
max_steering_angle = pi / 4  # You don't need to use this value, but it is good to keep in mind the limitations of a real car.


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
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))


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

    def move(self, motion, tolerance=0.001):  # Do not change the name of this function

        steering_angle = motion[0]
        distance_w = motion[1]

        result = robot()
        result.set_noise(self.bearing_noise, self.steering_noise, self.distance_noise)
        result.length = self.length
        steering_angle = random.gauss(steering_angle, result.steering_noise)
        distance_w = random.gauss(distance_w, result.distance_noise)

        turning_angle = distance_w * tan(steering_angle) / result.length

        if abs(turning_angle) > tolerance:
            radius = distance_w / turning_angle
            cx = self.x - sin(self.orientation) * radius
            cy = self.y + cos(self.orientation) * radius
            orientation = (self.orientation + turning_angle) % (2 * pi)
            x = cx + sin(orientation) * radius
            y = cy - cos(orientation) * radius

        else:
            x = self.x + cos(self.orientation) * distance_w
            y = self.y + sin(self.orientation) * distance_w
            orientation = (self.orientation + turning_angle) % (2 * pi)

        result.set(x, y, orientation)

        return result


length = 20.
bearing_noise = 0.0
steering_noise = 0.0
distance_noise = 0.0

myrobot = robot(length)
myrobot.set(0.0, 0.0, 0.0)
myrobot.set_noise(bearing_noise, steering_noise, distance_noise)

motions = [[0.2, 10.] for row in range(10)]

T = len(motions)
print ('Robot:    ', myrobot)

for t in range(T):
    myrobot = myrobot.move(motions[t])
    print ('Robot:    ', myrobot)


