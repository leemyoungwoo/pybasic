import csv

f = open('jeju_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)

sum_rain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in lines:
    if not line[5] :             
        line[5] = 0
        
    if int(line[2][5:7]) == 1 :    # 1월 이면
        sum_rain[0] += float(line[5])
    if int(line[2][5:7]) == 2 :    # 2월 이면
        sum_rain[1] += float(line[5])
    if int(line[2][5:7]) == 3 :    # 3월 이면
        sum_rain[2] += float(line[5])
    if int(line[2][5:7]) == 4 :    # 4월 이면
        sum_rain[3] += float(line[5])
    if int(line[2][5:7]) == 5 :    # 5월 이면
        sum_rain[4] += float(line[5])
    if int(line[2][5:7]) == 6 :    # 6월 이면
        sum_rain[5] += float(line[5])
    if int(line[2][5:7]) == 7 :    # 7월 이면
        sum_rain[6] += float(line[5])
    if int(line[2][5:7]) == 8 :    # 8월 이면
        sum_rain[7] += float(line[5])
    if int(line[2][5:7]) == 9 :    # 9월 이면
        sum_rain[8] += float(line[5])
    if int(line[2][5:7]) == 10 :    # 10월 이면
        sum_rain[9] += float(line[5])
    if int(line[2][5:7]) == 11 :    # 11월 이면
        sum_rain[10] += float(line[5])
    if int(line[2][5:7]) == 12 :    # 12월 이면
        sum_rain[11] += float(line[5])                

max_month_rain = max(sum_rain)
max_month = sum_rain.index(max_month_rain) + 1

print('(1) 최대 강수 월과 강수량 : %d월, %.1f mm\n' % (max_month, max_month_rain))
print('(2) 월별 강수량')

for i in range(1, 13) :
    print('%d월 : %.1f mm' % (i, sum_rain[i-1]))

f.close()