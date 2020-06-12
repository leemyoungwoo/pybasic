scores = {'김예진': 90, '박영진': 95, '김소희': 84}

sum = 0
for key in scores :
    sum += scores[key]

    print('%s : %d' % (key , scores[key]))
    
avg = sum/len(scores)

print('합계 : %d, 평균 : %.2f' % (sum, avg ))