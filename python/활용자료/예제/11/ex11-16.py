import csv

f = open('jeju_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)

month = 7    # 기준 월
min_humidity = 1000
max_humidity = -1000

for line in lines:
    if line[1] == '고산' and int(line[2][5:7]) == month :
        if float(line[6]) < min_humidity :
            min_humidity = float(line[6])
        
        if float(line[6]) > max_humidity :
            max_humidity = float(line[6])

print('%d월 최저 습도 : %.1f' % (month, min_humidity))
print('%d월 최대 습도 : %.1f' % (month, max_humidity))

f.close()