scores = []

while True :
    score = int(input('성적을 입력하세요(종료 시 -1 입력): '))

    if score == -1 :
        break
    else :
        scores.append(score)

sum = 0
for i in range(0, len(scores)) :
    sum += scores[i]

avg = sum/len(scores)

print('합계 : %d, 평균 : %.2f' % (sum, avg))