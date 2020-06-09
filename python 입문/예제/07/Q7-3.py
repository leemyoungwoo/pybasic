def computeMaxGong(x, y):
    if x > y:
        small = y
    else:
        small = x
        
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            result = i
    return result

num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))

max_gong = computeMaxGong(num1, num2)

print('%d과(와) %d의 최대공약수 : %d' % (num1, num2, max_gong))