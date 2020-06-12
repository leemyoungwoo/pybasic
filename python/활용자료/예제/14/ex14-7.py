import pandas as pd

data = {'이름':['홍지수', '안지영', '김성수', '최예린'],
        '아이디' : ['jshong', 'jyahn', 'sukim', 'yrchoi'],
        '비밀번호' : ['1234', '1234', '1234', '1234']}

frame = pd.DataFrame(data)
print(frame)