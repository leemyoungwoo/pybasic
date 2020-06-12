import numpy as np

a = np.array([[10, 20, 30],
              [15, 7, 55],
              [5, 33, 12]])

print(np.argmax(a, axis=0))
print(np.argmax(a, axis=1))