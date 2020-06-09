import csv

f = open('month_temp.csv', 'r', encoding='utf-8')
lines = csv.reader(f)
header = next(lines)

print(header)

f.close()