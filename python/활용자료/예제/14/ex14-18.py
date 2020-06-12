import population as pop
import pandas as pd
from matplotlib import rc
rc('font', family='Malgun Gothic')

list_data = []

# CSV 파일을 읽어 들여 리스트 list_data에 저장
pop.get_list(list_data)         

# 딕셔너리 dict_data를 위한 키 설정
keys = ['지역', '총인구수', '세대수', '세대당_인구', '남자_인구수', '여자_인구수', '남여_비율']

dict_data = {}

# 리스트 list_data와 딕셔너리의 키 keys를 딕셔너리 dict_data에 저장
pop.get_dict(list_data, keys, dict_data)              

frame = pd.DataFrame(dict_data)
index = ['서울', '부산', '대구', '인천', '광주', '대전']

x1 = frame.iloc[:6, 1]
x1 = x1.values.tolist()

x2 = frame.iloc[:6, 2]
x2 = x2.values.tolist()

df = pd.DataFrame({'총인구수':x1, '총세대수':x2}, index=index)
ax = df.plot.bar(rot=0)