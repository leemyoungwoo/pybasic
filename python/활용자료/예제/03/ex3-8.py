age = int(input('나이를 입력하세요 : '))
pay = '3000원'

if age >= 65 or age < 7 :
    pay = '무료'

print('입장료 : %s' % pay)