char = input('영어 알파벳을 입력하세요 : ')

char2 = char.upper()

if char2 == 'A' or char2 == 'E' or char2 == 'I' or char2 == 'O' or char2 == 'U' :
    print('%s은(는) 모음이다.' % char)
else :
    print('%s은(는) 자음이다.' % char)