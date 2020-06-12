def maxTwo(i, j):
    if i > j:
        return i
    else :
        return j

def maxThree(x, y, z) :
    max1 = maxTwo(x, y)
    max2 = maxTwo(y, z)
    
    if max1 > max2 : 
        largest = max1
    else :
        largest = max2
            
    return largest

a = int(input('첫 번째 수를 입력하세요: '))
b = int(input('두 번째 수를 입력하세요: '))
c = int(input('세 번째 수를 입력하세요: '))

max_num = maxThree(a, b, c)

print('%d, %d, %d 중 가장 큰 수 : %d' % (a, b, c, max_num))