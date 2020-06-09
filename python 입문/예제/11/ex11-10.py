import csv

f = open('pharm_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)
print('번호', header[1], header[0], header[4], header[5], sep=',')

number = 1
for line in lines:
    if ('경상북도' in line[2]) and (int(line[3])>=20100101 and int(line[3])<=20101231):
        print(number, '.', sep='', end=' ')
        print(line[1], line[0],  line[4], line[5], sep='/')
        number += 1

f.close()