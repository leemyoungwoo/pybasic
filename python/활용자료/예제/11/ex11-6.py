import csv

file1 = open('month_temp.csv', 'r', encoding='utf-8')
file2 = open('month_temp2.csv', 'w', encoding='utf-8', newline='')
lines = csv.reader(file1)
wr = csv.writer(file2)

wr.writerow(['일자', '최저기온', '최고기온', '일교차'])
next(lines)
for line in lines:
    diff = float(line[4]) - float(line[3])
    diff = format(diff, '.1f')
    wr.writerow([line[1], float(line[3]), float(line[4]), diff])

print('파일 쓰기 완료!')
file1.close()
file2.close()