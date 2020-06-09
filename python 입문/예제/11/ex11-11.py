import csv

f = open('pharm_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)
print('번호', header[0], header[2], sep=',')

data = []

for line in lines:
    if line[1] == '용인수지구'  :
        tmp = '%s/%s' % (line[0], line[2])
        data.append(tmp)

data.sort()

number = 1
for x in data :
    print('%d. %s' % (number, x))
    number += 1
    
f.close()