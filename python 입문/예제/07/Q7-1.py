def sum(start, end) :
    total = 0
    for i in range(start, end+1) :
        total += i
    print('%d ~ %d의 정수 합계 : %d' % (start, end, total))
    
sum(10, 100)
sum(100, 1000)
sum(1000, 10000)