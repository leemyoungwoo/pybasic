import numpy as np

data = np.random.randn(3,4)
print(data)

print(data > 0)

total = (data < 0).sum()   # 음수의 원소 개수
print(total)

data2 = np.where(data > 0, 1, -1)
print(data2)

data3 = np.where(data > 0, 5, data)
print(data3)