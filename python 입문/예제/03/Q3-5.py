height = int(input('키를 입력해 주세요 : '))
weight = int(input('몸무게를 입력해 주세요 : '))

a = (height - 100) * 0.9;  

print('-' * 30)
print('키 : %dcm' % height)
print('몸무게 : %dkg' % weight)

if weight > a:
    print('딱 보기 좋습니다.')
else :
    print('표준(또는 마른) 체형입니다.')

print('-' * 30)