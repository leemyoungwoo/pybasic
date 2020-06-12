import numpy as np

data = np.array([[13, 22, 17, 2],
             [-2, 20, 8, 3], 
             [-16, 10, -5, 33]])

data.sort(0)
print(data)
print()

data.sort(1)
print(data)