import pandas as pd

pop = pd.Series({'서울':9765623, '부산':3441453, '대구':2461769}, index = ['서울', '부산', '대구', '광주', '대전'])
print(pop)

pop['광주'] = 149336

print('광주시 인구 : %.0f명' % pop['광주'])