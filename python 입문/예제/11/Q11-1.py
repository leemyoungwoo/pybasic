import csv

f = open('month_temp.csv', 'r', encoding='utf-8')
lines = csv.reader(f)
for line in lines:
    for x in line:
        print('%s' % x, end='/')
    print()
f.close()