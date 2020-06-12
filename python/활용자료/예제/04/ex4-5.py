sum = 0
for i in range(1, 101) :
    if i%3 == 0 :
        print('%d' % i, end = ' ')
        sum += i

print('\n','-' * 50)
print('1~100에서 3의 배수의 합계 : %d' % sum)