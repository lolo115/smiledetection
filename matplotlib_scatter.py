import numpy as np
import matplotlib.pyplot as plt

num_points = 5000
dimensions = 2
points = np.random.normal(0, 1000, [num_points, dimensions])

#print('points[0]',points[:,0])
#print('points[1]',points[:,1])
print('points = \n',points)


plt.scatter(points[:,0], points[:,1])
plt.show()

