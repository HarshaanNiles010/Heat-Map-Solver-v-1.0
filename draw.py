from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


np.random.seed(1234)
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
A = np.random.randint(5, size=(25, 10))

x = np.array([[i] * 10 for i in range(25)]).ravel() # x coordinates of each bar
y = np.array([i for i in range(10)] * 25) # y coordinates of each bar
z = np.zeros(25*10) # z coordinates of each bar
dx = np.ones(25*10) # length along x-axis of each bar
dy = np.ones(25*10) # length along y-axis of each bar
dz = A.ravel() # length along z-axis of each bar (height)

ax1.bar3d(x, y, z, dx, dy, dz)