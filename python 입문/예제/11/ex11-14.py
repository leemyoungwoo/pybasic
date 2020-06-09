import csv

f = open('jeju_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)

month = 8    # 기준 월

max_jeju = -1000
max_sungsan = -1000
max_gosan = -1000
max_suguipo = -1000

for line in lines:
    if line[1] == '제주' and int(line[2][5:7]) == month :
        if float(line[4]) > max_jeju :
            max_jeju = float(line[4])
    
    if line[1] == '고산' and int(line[2][5:7]) == month :
        if float(line[4]) > max_gosan :
            max_gosan = float(line[4])
    
    if line[1] == '성산' and int(line[2][5:7]) == month :
        if float(line[4]) > max_sungsan :
            max_sungsan = float(line[4])
            
    if line[1] == '서귀포' and int(line[2][5:7]) == month :
        if float(line[4]) > max_suguipo :
            max_suguipo = float(line[4])
            
print('%d월 제주 최고기온 : %.1f' % (month, max_jeju))
print('%d월 고산 최고기온 : %.1f' % (month, max_gosan))
print('%d월 성산 최고기온 : %.1f' % (month, max_sungsan))
print('%d월 서귀포 최고기온 : %.1f' % (month, max_suguipo))

f.close()