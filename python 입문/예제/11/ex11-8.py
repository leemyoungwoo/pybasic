import csv

f = open('pharm_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)

for line in lines:
    if ('수지' in line[2]) and ('로얄스포츠' in line[2]):
        print(line[2], line[0], line[3], sep='/')

f.close()