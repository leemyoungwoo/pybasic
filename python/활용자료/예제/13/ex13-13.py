import csv
import numpy as np

f = open('school_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)

list_data = []
for line in lines :
    list_data.append(line[:])

length = len(list_data)
print(length)

data = np.zeros((length, 3), dtype='int32')

for i in range(length) :
    for j in range(3) :
        data[i][j] = list_data[i][j+2]
        
print(data)

f.close()