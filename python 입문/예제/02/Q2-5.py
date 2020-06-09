name = input('학생 이름을 입력하세요 :')
kor = int(input('국어 성적을 입력하세요 :'))
eng = int(input('영어 성적을 입력하세요 :'))
math = int(input('수학 성적을 입력하세요 :'))

total = kor + eng + math
avg = total / 3

print('이름:%s, 국어:%d, 영어:%d,수학:%d, 평균:%.1f점' % (name, kor, eng, math, avg))