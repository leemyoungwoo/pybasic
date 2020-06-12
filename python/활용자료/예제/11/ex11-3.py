import csv

f = open('month_temp.csv', 'r', encoding='utf-8')
lines = csv.reader(f)
for line in lines:
    if '2019-10-20' in line:
        print(line)
f.close()