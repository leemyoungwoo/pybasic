num = int(input('숫자를 입력하세요 : '))
result = '4의 배수도 5의 배수도 아니다.'

if num%4 == 0 :
    result = '4의 배수이다'    
if num%5 == 0 :
    result = '5의 배수이다'
if num%4 == 0 and num%5 == 0 :
    result = '4의 배수이면서 5의 배수이다.'

print('%d은(는) %s' % (num, result))