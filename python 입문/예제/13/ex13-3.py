import numpy as np

data1 = np.zeros(10)
print(data1)
print(data1.dtype)

data2 = np.zeros((2, 3))
print(data2)

data3 = np.zeros((2, 3), dtype=np.int32)
print(data3)