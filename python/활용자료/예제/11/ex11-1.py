import csv

f = open('month_temp.csv', 'r', encoding='utf-8')
lines = csv.reader(f)
for line in lines:
    print(line)
f.close()