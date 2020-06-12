import pandas as pd

pop = pd.Series([9765623, 3441453, 2461769], index=['서울', '부산', '대구'])

for i, v in pop.items() :
    print('%s : %d명' % (i, v))