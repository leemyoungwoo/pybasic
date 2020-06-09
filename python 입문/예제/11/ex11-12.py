import csv

f = open('jeju_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)
print(header[1], header[2], header[3])

for line in lines:
    if line[1] == '서귀포' and line[2][5:7] == '01':
        print(line[1], line[2], line[3])

f.close()