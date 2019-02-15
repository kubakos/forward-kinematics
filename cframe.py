#!/usr/bin/env python
from math import radians, sin, cos
import numpy as np



class CoordinateFrame(object):
    """ Creates a coordinate frame as a homogeneous matrix. """


    def __init__(self, base = None):

        # [0,0] - [2,2] rotation
        # [0,3] - [2,3] position
        # [3,0] - [3,2] perspective parameters
        # [3,3] scale factor
        self.matrix = np.identity(4)


    def __getitem__(self, key):
        return self.matrix[key]


    def get(self):
        return self.matrix


    def roll(self, angle_X):
        """ Rotates the homogeneous matrix by angle_X by the X axis. """
        rolled_by = np.array([
                    [1,                     0,                        0],
                    [0, cos(radians(angle_X)), -(sin(radians(angle_X)))],
                    [0, sin(radians(angle_X)),        cos(radians(angle_X))] ])
        h_rot= np.array([
                    [self.matrix[0,0], self.matrix[0,1], self.matrix[0,2]],
                    [self.matrix[1,0], self.matrix[1,1], self.matrix[1,2]],
                    [self.matrix[2,0], self.matrix[2,1], self.matrix[2,2]] ])

        h_rot = np.dot(h_rot, rolled_by)

        for i in range(3):
            for j in range(3):
                self.matrix[i, j] = h_rot[i, j]




    def pitch(self, angle_Y):
        """ Rotates the homogeneous matrix by angle_Y by the Y axis. """
        pitched_by = np.array([
                    [   cos(radians(angle_Y)), 0, sin(radians(angle_Y))],
                    [                       0, 1, 0                    ],
                    [-(sin(radians(angle_Y))), 0, cos(radians(angle_Y))] ])
        h_rot = np.array([
                    [self.matrix[0,0], self.matrix[0,1], self.matrix[0,2]],
                    [self.matrix[1,0], self.matrix[1,1], self.matrix[1,2]],
                    [self.matrix[2,0], self.matrix[2,1], self.matrix[2,2]] ])

        h_rot = np.dot(h_rot, pitched_by)

        for i in range(3):
            for j in range(3):
                self.matrix[i, j] = h_rot[i, j]




    def yaw(self, angle_Z):
        """ Rotates the homogeneous matrix by angle_Z by the Z axis. """
        yawed_by = np.array([
                    [cos(radians(angle_Z)), -(sin(radians(angle_Z))), 0],
                    [sin(radians(angle_Z)),    cos(radians(angle_Z)), 0],
                    [                    0,                        0, 1] ])
        h_rot = np.array([
                    [self.matrix[0,0], self.matrix[0,1], self.matrix[0,2]],
                    [self.matrix[1,0], self.matrix[1,1], self.matrix[1,2]],
                    [self.matrix[2,0], self.matrix[2,1], self.matrix[2,2]] ])

        h_rot = np.dot(h_rot, yawed_by)

        for i in range(3):
            for j in range(3):
                self.matrix[i, j] = h_rot[i, j]




    def setDH(self, a, alpha, d, theta):
        """
        Sets the relation between two coordinate frames using the
        Denavit-Hartenberg Convention.

        a:
        alpha:
        d:
        theta:

        Format: ([ax, ay], ["X/Y", alpha], d, theta)
        """

        # Setting a:
        self.matrix[0,3] = self.matrix[0,3] + a[0]
        self.matrix[1,3] = self.matrix[1,3] + a[1]

        # Setting alpha:
        if alpha[0] == "x":
            self.roll(alpha[1])
        elif alpha[0] == "y":
            self.pitch(alpha[1])

        # Setting d:
        self.matrix[2,3] = self.matrix[2,3] + d

        # Setting theta:
        self.yaw(theta)
