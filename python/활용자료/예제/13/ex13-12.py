import csv

f = open('school_2019.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

header = next(lines)
print(header)

list_data = []
for line in lines :
    list_data.append(line[:])

print(list_data)
f.close()