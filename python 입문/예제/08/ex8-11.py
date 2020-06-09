import random

again = 'y'
count = 1

while again =='y':
    print('-' * 30)
    print('주사위 던지기 : %d번째' % count)
    me = random.randint(1, 6)
    computer = random.randint(1, 6)
    print('나 : %d' % me )
    print('컴퓨터 : %d' % computer)
    
    if me > computer :
        print('나의 승리!')
    elif me == computer :
        print('무승부!')
    else :
        print('컴퓨터의 승리!')
    
    count = count + 1
    again = input('계속하려면 y를 입력하세요!')