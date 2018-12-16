#!/usr/bin/env python
from math import radians, sin, cos
from numpy import array, dot


class cframe(object):
    """ Creates a coordinate frame as a homogeneous matrix. """
    
    
    def __init__(self, homogen = None):
        
        # [0,0] - [2,2] are rotation, [0,3] - [2,3] position,
        # [3,0] - [3,2] are perspective parameters,
        # [3,3] is the scale factor
        
        if homogen is None:
            self.h_matrix = array([
                            [1.0, 0.0, 0.0, 0.0],
                            [0.0, 1.0, 0.0, 0.0],
                            [0.0, 0.0, 1.0, 0.0],
                            [0.0, 0.0, 0.0, 1.0] ])
        else:
            self.h_matrix = homogen.getMatrix()



    def __getitem__(self, i, j):
        return self.h_matrix[i, j]



    def setRoll(self, angle_X):
        """ Rotates the homogeneous matrix by angle_X by the X axis. """
        rolled_by = array([
                    [1,                     0,                        0],
                    [0, cos(radians(angle_X)), -(sin(radians(angle_X)))],
                    [0, sin(radians(angle_X)),        cos(radians(angle_X))] ])
        h_rot= array([
                    [self.h_matrix[0,0], self.h_matrix[0,1], self.h_matrix[0,2]],
                    [self.h_matrix[1,0], self.h_matrix[1,1], self.h_matrix[1,2]],
                    [self.h_matrix[2,0], self.h_matrix[2,1], self.h_matrix[2,2]] ])

        h_rot = dot(h_rot, rolled_by)
        
        for i in range(3):
            for j in range(3):
                self.h_matrix[i, j] = h_rot[i, j]




    def setPitch(self, angle_Y):
        """ Rotates the homogeneous matrix by angle_Y by the Y axis. """
        pitched_by = array([
                    [   cos(radians(angle_Y)), 0, sin(radians(angle_Y))],
                    [                       0, 1, 0                    ],
                    [-(sin(radians(angle_Y))), 0, cos(radians(angle_Y))] ])
        h_rot = array([
                    [self.h_matrix[0,0], self.h_matrix[0,1], self.h_matrix[0,2]],
                    [self.h_matrix[1,0], self.h_matrix[1,1], self.h_matrix[1,2]],
                    [self.h_matrix[2,0], self.h_matrix[2,1], self.h_matrix[2,2]] ])

        h_rot = dot(h_rot, pitched_by)

        for i in range(3):
            for j in range(3):
                self.h_matrix[i, j] = h_rot[i, j]
    



    def setYaw(self, angle_Z):
        """ Rotates the homogeneous matrix by angle_Z by the Z axis. """
        yawed_by = array([
                    [cos(radians(angle_Z)), -(sin(radians(angle_Z))), 0],
                    [sin(radians(angle_Z)),    cos(radians(angle_Z)), 0],
                    [                    0,                        0, 1] ])
        h_rot = array([
                    [self.h_matrix[0,0], self.h_matrix[0,1], self.h_matrix[0,2]],
                    [self.h_matrix[1,0], self.h_matrix[1,1], self.h_matrix[1,2]],
                    [self.h_matrix[2,0], self.h_matrix[2,1], self.h_matrix[2,2]] ])

        h_rot = dot(h_rot, yawed_by)

        for i in range(3):
            for j in range(3):
                self.h_matrix[i, j] = h_rot[i, j]
    



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
        self.h_matrix[0,3] = self.h_matrix[0,3] + a[0]
        self.h_matrix[1,3] = self.h_matrix[1,3] + a[1]
        
        # Setting alpha:
        if alpha[0] == "x":
            self.setRoll(alpha[1])
        elif alpha[0] == "y":
            self.setPitch(alpha[1])
        
        # Setting d:
        self.h_matrix[2,3] = self.h_matrix[2,3] + d
        
        # Setting theta:
        self.setYaw(theta)



    def get(self):
        """ Returns the homogeneous matrix itself. """
        return self.h_matrix




'''
class Link(Cframe):
    def __init__(self):
        pass
'''





