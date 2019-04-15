#!/usr/bin/env python3
# https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to

#
# Jointangles of the wireframe robot can be changed
# via the set_param_theta() method of the
# CoordinateFrame object in the 'Robotic Arm construction'
# section
#

from cframe import CoordinateFrame
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


# Robotic Arm construction

base = CoordinateFrame()
joint1 = CoordinateFrame()
joint2 = CoordinateFrame()
joint3 = CoordinateFrame()
joint4 = CoordinateFrame()
joint5 = CoordinateFrame()
joint6 = CoordinateFrame()

joint1.set_param_d(100)
joint1.set_param_theta(0)

joint2.set_param_alpha(90, 0)
joint2.set_param_theta(110)

joint3.set_param_a(300, 0)
joint3.set_param_theta(-150)

joint4.set_param_a(150, 0)
joint4.set_param_alpha(0, 90)
joint4.set_param_theta(0)

joint4.set_param_alpha(0, -90)
joint5.set_param_a(100, 0)
joint5.set_param_theta(40)

joint6.set_param_a(30, 0)
joint6.set_param_theta(0)

joint1.set_parent(base.get())
joint2.set_parent(joint1.get())
joint3.set_parent(joint2.get())
joint4.set_parent(joint3.get())
joint5.set_parent(joint4.get())
joint6.set_parent(joint5.get())

# Prepare the coordinates for plotting

X = [base[0, 3], joint1[0, 3],
     joint2[0, 3], joint3[0, 3],
     joint4[0, 3], joint5[0, 3],
     joint6[0, 3]]
Y = [base[1, 3], joint1[1, 3],
     joint2[1, 3], joint3[1, 3],
     joint4[1, 3], joint5[1, 3],
     joint6[1, 3]]
Z = [base[2, 3], joint1[2, 3],
     joint2[2, 3], joint3[2, 3],
     joint4[2, 3], joint5[2, 3],
     joint6[2, 3]]

# Plot

ax = plt.axes(projection='3d')
ax.set_aspect('equal')
ax.plot3D(X, Y, Z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

set_axes_equal(ax)
plt.show()
