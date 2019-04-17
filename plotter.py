#!/usr/bin/env python3
# https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to

from tf import HomogeneousMatrix
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


base = HomogeneousMatrix()
joint1 = HomogeneousMatrix()
joint2 = HomogeneousMatrix()
joint3 = HomogeneousMatrix()
joint4 = HomogeneousMatrix()
joint5 = HomogeneousMatrix()
joint6 = HomogeneousMatrix()

# --- Robotic Arm construction ---

#    Joint Angle variables

q1, q2, q3 = 0, 110, -130
q4, q5, q6 = 0, 40, 0

#    ---------------------

joint1.set_d(100)
joint1.set_theta(q1)

joint2.set_alpha(90)
joint2.set_theta(q2)

joint3.set_a(300)
joint3.set_theta(q3)

joint4.set_a(250)
joint4.set_theta(-90)
joint4.set_alpha(-90)
joint4.set_theta(q4)

joint5.set_alpha(90)
joint5.set_theta(90)
joint5.set_theta(q5)

joint6.set_theta(-90)
joint6.set_alpha(-90)
joint6.set_a(30)
joint6.set_theta(q6)

# ---------------------------------

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
