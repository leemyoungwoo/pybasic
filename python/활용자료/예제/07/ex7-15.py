scores = ['김소영 82 80 93 97 93 88',
           '정예린 86 100 93 86 90 77',
           '이세영 91 88 99 79 92 68',
           '정수정 86 100 93 89 92 93',
           '박지수 80 100 95 89 90 84']
data = ''
for item in scores :
    data += item + '\n'

# 화면 출력하기    
print(data)

# 파일(scores.txt)에 저장하기
file = open('scores.txt', 'w', encoding='utf8' )
file.write(data)
file.close()