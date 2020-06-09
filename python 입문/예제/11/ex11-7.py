import csv

f = open('pharm_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)

for line in lines:
    if line[1] == '경주시' and line[0] == '신대원약국':
        print(line[0], line[1], line[2], sep='/')

f.close()