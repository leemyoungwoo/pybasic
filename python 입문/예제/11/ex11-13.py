import csv

f = open('jeju_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)

month = 1    # 기준 월
sum = 0
num_day = 0

for line in lines:
    if line[1] == '서귀포' and int(line[2][5:7]) == month :
        sum += float(line[3])
        num_day += 1
        
avg = sum/num_day

print('%d월 일수 : %d' % (month, num_day))
print('%d월 최저기온 평균 : %.1f' % (month, avg))

f.close()