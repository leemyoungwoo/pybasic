import csv

f = open('month_temp.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

next(lines)             # 헤더를 건너뛴다.

sum = 0
for line in lines:
    if (int(line[1][8:]) <= 10) :
        sum += float(line[2])

avg = sum/3
print('10일간 평균 기온 : %.1f' % avg)

f.close()