import csv

f = open('month_temp.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

print('%s %s %s %s' % ('일자', '최저기온', '최고기온', '일교차'))

next(lines)             # 헤더를 건너뛴다.
for line in lines:
    diff = float(line[4]) - float(line[3])
    print('%s %.1f %.1f %.1f' % (line[1], float(line[3]), float(line[4]), diff))

f.close()