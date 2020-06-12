import numpy as np

data = np.arange(10, 121, 10)
print(data)
print(data[2])
print(data[5:8])

data[7:10] = 800
print(data)

data2 = data.reshape(2, 6)
print(data2)