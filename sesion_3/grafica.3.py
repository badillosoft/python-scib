import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 4 * np.pi, 1000)

a = 0.2

r = 2 * a * np.sin(theta) * np.cos(theta)

fig = plt.figure()

ax = fig.add_subplot(221, projection='polar')

ax.plot(theta, r)

plt.show()