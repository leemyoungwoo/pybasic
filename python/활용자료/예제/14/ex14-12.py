import pandas as pd

scores = {'이름': ['김지영', '안지수', '최성수', '황예린', '김소정'],
        '국어' : [95, 97, 90, 94, 87],
        '영어' : [90, 86, 93, 85, 93],
        '수학' : [85, 88, 89, 88, 99]}

frame = pd.DataFrame(scores)
frame2 = frame.iloc[:, [1, 2, 3]]

total = frame2.sum(axis = 1)
avg = frame2.mean(axis = 1)

print('-' * 50)
print('이름    합계  평균')
print('-' * 50)
for i in range(5) :
    print('%s  %d   %.2f' % (frame.iloc[i, 0], total.iloc[i], avg.iloc[i]))
    
print('-' * 50)    