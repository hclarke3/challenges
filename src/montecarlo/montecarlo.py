import numpy as np
import matplotlib.pyplot as plt

#constants
RADIUS = 500
NUMPOINTS = 100000

# arrays for processing
points = np.random.rand(NUMPOINTS,2)
points = [[x*1000, y*1000] for x,y in points]
print points
points_in_circle = []

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(points, '.r')

circ = plt.Circle((RADIUS, RADIUS), radius=RADIUS, color='b', alpha=0.15)
ax.add_patch(circ)

plt.xlim(0,2*RADIUS)
plt.ylim(0,2*RADIUS)

# run the math
for x,y in points:
    if ((x - RADIUS)**2 + (y - RADIUS)**2) < RADIUS**2:
        points_in_circle.append([x,y])

pi = (float(len(points_in_circle) * 4)) / float(NUMPOINTS)
ax.set_title(r"$\pi = "+str(pi)+"$")

plt.show()
