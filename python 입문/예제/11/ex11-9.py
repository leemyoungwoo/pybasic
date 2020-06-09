import csv
f = open('pharm_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)

city = '원주시'
total = 0
recent = 0
for line in lines:
    if line[1] == city :
        count += 1
        if int(line[3]) > 20140901 :
            recent += 1

print('%s의 약국 수 : %d개' % (city, count))
print('5년 이내 개설된 약국 수 : %d개' % recent)