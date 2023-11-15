#!/usr/bin/env python3
import constructor

if __name__ == '__main__':
    x = constructor.ArmConstructor()
    x.set_joint_angles(q1=0, q2=110, q3=-150, q4=0, q5=40, q6=0)
    x.plot_arm()
