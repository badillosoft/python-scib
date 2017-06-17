import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234, projection="polar")
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)

ax1.plot([1, 2, 3], [1, 2, 3])

ax2.pie([50, 20, 34])
ax2.axis("equal")

x = np.linspace(-1, 1, 40)
y = np.exp(x)
ax3.plot(x, y, "g")

ax4.plot([0, np.pi / 4., np.pi / 2], [1, 2, 3])

ax5.plot([1, 2, 3], [3, 2, 1])

ax6.pie([23, 1, 2])
ax6.axis("equal")

plt.show()