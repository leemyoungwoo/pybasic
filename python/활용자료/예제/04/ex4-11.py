n1 = int(input('첫 수를 입력하세요 : '))
n2 = int(input('끝 수를 입력하세요 : '))
n = int(input('합계를 구하고자 하는 배수를 입력하세요 : '))

sum = 0
i = n1

while i < n2+1 :
    if i%n == 0 :
        sum += i

    i += 1
    
print('%d~%d까지의 정수 중 %d의 배수의 합계 : %d' % (n1, n2, n, sum))