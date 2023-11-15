import matplotlib.pyplot as plt
import numpy as np
import tf


class ArmConstructor:

    def __init__(self):
        self.base = tf.HomogeneousMatrix()
        self.joint1 = tf.HomogeneousMatrix()
        self.joint2 = tf.HomogeneousMatrix()
        self.joint3 = tf.HomogeneousMatrix()
        self.joint4 = tf.HomogeneousMatrix()
        self.joint5 = tf.HomogeneousMatrix()
        self.joint6 = tf.HomogeneousMatrix()
        self.joint1.set_d(100)
        self.joint2.set_alpha(90)
        self.joint3.set_a(300)
        self.joint4.set_a(250)
        self.joint4.set_theta(-90)
        self.joint4.set_alpha(-90)
        self.joint5.set_alpha(90)
        self.joint5.set_theta(90)
        self.joint6.set_theta(-90)
        self.joint6.set_alpha(-90)
        self.joint6.set_a(30)

    def set_joint_angles(self, q1=0, q2=110, q3=-150, q4=0, q5=40, q6=0):
        self.joint1.set_theta(q1)
        self.joint2.set_theta(q2)
        self.joint3.set_theta(q3)
        self.joint4.set_theta(q4)
        self.joint5.set_theta(q5)
        self.joint6.set_theta(q6)

    def construct_arm(self):
        self.joint1.set_parent(self.base.get())
        self.joint2.set_parent(self.joint1.get())
        self.joint3.set_parent(self.joint2.get())
        self.joint4.set_parent(self.joint3.get())
        self.joint5.set_parent(self.joint4.get())
        self.joint6.set_parent(self.joint5.get())

    def set_axes_equal(self, ax):
        x_limits = ax.get_xlim3d()
        y_limits = ax.get_ylim3d()
        z_limits = ax.get_zlim3d()

        x_range = abs(x_limits[1] - x_limits[0])
        x_middle = np.mean(x_limits)
        y_range = abs(y_limits[1] - y_limits[0])
        y_middle = np.mean(y_limits)
        z_range = abs(z_limits[1] - z_limits[0])
        z_middle = np.mean(z_limits)

        plot_radius = 0.5*max([x_range, y_range, z_range])
        ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
        ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
        ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

    def plot_arm(self):
        self.construct_arm()
        X = [self.base[0, 3], self.joint1[0, 3],
             self.joint2[0, 3], self.joint3[0, 3],
             self.joint4[0, 3], self.joint5[0, 3],
             self.joint6[0, 3]]
        Y = [self.base[1, 3], self.joint1[1, 3],
             self.joint2[1, 3], self.joint3[1, 3],
             self.joint4[1, 3], self.joint5[1, 3],
             self.joint6[1, 3]]
        Z = [self.base[2, 3], self.joint1[2, 3],
             self.joint2[2, 3], self.joint3[2, 3],
             self.joint4[2, 3], self.joint5[2, 3],
             self.joint6[2, 3]]

        ax = plt.axes(projection='3d')
        ax.set_aspect('equal')
        ax.plot3D(X, Y, Z)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        self.set_axes_equal(ax)
        plt.show()
