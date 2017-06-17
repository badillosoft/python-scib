import numpy as np

A = np.array([
    [2, 1],
    [1, 10]
])

b = np.array([10, 24])

Ap = np.linalg.inv(A)

x = Ap.dot(b)

print x

print np.linalg.solve(A, b)
