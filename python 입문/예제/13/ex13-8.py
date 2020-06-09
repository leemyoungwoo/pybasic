import numpy as np

data = np.array([[80, 78, 90, 93],
                 [65, 87, 88, 75], 
                 [98, 100, 68, 80]])

print(data.sum())
print(data.mean())
print(data.max())
print(data.min())
print()

print(data.max(axis=0))
print(data.max(axis=1))
print()

index1 = np.argmax(data, axis=0)
index2 = np.argmin(data, axis=1)
print(index1, index2)