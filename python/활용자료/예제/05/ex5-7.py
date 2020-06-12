scores = [88, 75, 90, 95, 77, 69, 80, 92]

sum = 0
for score in scores :
    sum += score
    
avg = sum/8

print('총점 : %d, 평균 : %.2f' % (sum, avg))