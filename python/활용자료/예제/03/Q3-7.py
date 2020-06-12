num1 = int(input('첫 번째 정수를 입력하세요 : ')) 
num2 = int(input('두 번째 정수를 입력하세요 : ')) 
num3 = int(input('세 번째 정수를 입력하세요 : ')) 

if (num1 >= num2) and (num1 >= num3): 
   largest = num1 
elif (num2 >= num1) and (num2 >= num3): 
   largest = num2 
else: 
   largest = num3 

print('입력된 세 수 %d, %d, %d 중에서 가장 큰 수는 %d 입니다.' % (num1, num2, num3, largest))