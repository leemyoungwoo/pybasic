import numpy as np

a = np.arange(10)
print(a)

b = np.insert(a, 3, 10)
print(b)

x = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(x)
print()

y = np.insert(x, 1, 10, axis=0)
print(y)

y = np.insert(x, 1, 10, axis=1)
print(y)