n1 = int(input('시작 수를 입력하세요 : '))
n2 = int(input('끝 수를 입력하세요 : '))

sum = 0
for i in range(n1, n2+1) :
    if i%5 != 0 :
        sum += i

print('-' * 50)
print('%d에서 %d까지 5의 배수가 아닌 수의 합계 : %d' % (n1, n2, sum))