#!/usr/bin/env python3
from cframe import CoordinateFrame
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

world = CoordinateFrame()

# Robotic Arm construction

base = CoordinateFrame(world)
base.set_pos(0, 0, 100)

joint1 = CoordinateFrame(base)
joint1.set_param_d(200)

joint2 = CoordinateFrame(joint1)
joint2.set_param_a(30, 0)
joint2.set_param_d(20)
joint2.set_param_alpha(90, 0)
joint2.set_param_theta(110)

joint3 = CoordinateFrame(joint2)
joint3.set_param_a(300, 0)
joint3.set_param_theta(120)

joint4 = CoordinateFrame(joint3)
joint4.set_param_a(250, 0)

# Prepare the coordinates for plotting

X = [world[0, 3], base[0, 3], joint1[0, 3],
     joint2[0, 3], joint3[0, 3], joint4[0, 3]]
Y = [world[1, 3], base[1, 3], joint1[1, 3],
     joint2[1, 3], joint3[1, 3], joint4[1, 3]]
Z = [world[2, 3], base[2, 3], joint1[2, 3],
     joint2[2, 3], joint3[2, 3], joint4[2, 3]]

# Plot

ax = plt.axes(projection='3d')
ax.plot3D(X, Y, Z)
plt.show()
