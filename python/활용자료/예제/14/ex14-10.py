import pandas as pd

data = {'아이디':['kim', 'song', 'han', 'choi'],
        '구매상품' : ['상품A', '상품B', '상품C', '상품D'],
        '가격' : [15000, 23000, 33000, 50000],
        '개수' : [3, 5, 1, 10],
        '구매일' : ['0303', '0810', '0120', '0601']}

frame = pd.DataFrame(data)
print(frame)

print(frame.iloc[2, 0])
print(frame.iloc[3, :2])
print(frame.iloc[:, [0, 4]])