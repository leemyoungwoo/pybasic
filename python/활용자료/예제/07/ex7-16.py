file = open('scores.txt', 'r', encoding='utf8')
lines = file.readlines()

print('scores.txt 파일의 내용 : ')
for line in lines :
    print(line, end='')
    
file.close()