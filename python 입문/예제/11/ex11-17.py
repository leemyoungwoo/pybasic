import csv

f = open('jeju_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)

total_rain = [0, 0, 0, 0]

for line in lines:
    if not line[5] :             
        line[5] = 0
        
    if line[1] == '제주' :    # '제주' 지역
        total_rain[0] += float(line[5])
        
    if line[1] == '고산' :    # '고산' 지역
        total_rain[1] += float(line[5])
        
    if line[1] == '성산' :    # '성산' 지역
        total_rain[2] += float(line[5])
        
    if line[1] == '서귀포' :    # '서귀포' 지역
        total_rain[3] += float(line[5])

max_year_rain = max(total_rain)

if total_rain.index(max_year_rain) == 0 :
    max_area = '제주'
if total_rain.index(max_year_rain) == 1 :
    max_area = '고산'
if total_rain.index(max_year_rain) == 2 :
    max_area = '성산'
if total_rain.index(max_year_rain) == 3 :
    max_area = '서귀포'    
    

print('(1) 연 강수 최대 지역: %s\n' % max_area)
print('(2) 지역별 강수량')
print('제주 : %.1f mm' % total_rain[0])
print('고산 : %.1f mm' % total_rain[1])
print('성산 : %.1f mm' % total_rain[2])
print('서귀포 : %.1f mm' % total_rain[3])

f.close()