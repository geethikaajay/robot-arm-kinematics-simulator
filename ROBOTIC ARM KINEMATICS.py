import numpy as np
import matplotlib.pyplot as plt

# link lengths
L1 = 2
L2 = 1.5

# joint angles (degrees)
theta1 = np.radians(45)
theta2 = np.radians(30)

# forward kinematics equations
x1 = L1 * np.cos(theta1)
y1 = L1 * np.sin(theta1)

x2 = x1 + L2 * np.cos(theta1 + theta2)
y2 = y1 + L2 * np.sin(theta1 + theta2)

# plot arm
plt.figure()

plt.plot([0, x1], [0, y1], marker='o')
plt.plot([x1, x2], [y1, y2], marker='o')

plt.xlim(-4,4)
plt.ylim(-4,4)

plt.title("2-Link Robot Arm Forward Kinematics")

plt.xlabel("X position")
plt.ylabel("Y position")

plt.grid()

plt.savefig("robot_arm_output.png")

plt.show()