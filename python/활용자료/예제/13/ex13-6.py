import numpy as np

data = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15]])

print(data)
print(data[2][3])
print(data[0][1:])
print(data[0])
print(data[[1, 2]])
print()

data[1]= 100
print(data)

data[:] = 200
print(data)