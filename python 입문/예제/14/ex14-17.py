import population as pop
import pandas as pd

list_data = []

# CSV 파일을 읽어 들여 리스트 list_data에 저장
pop.get_list(list_data)         

dict_data = {}

# 딕셔너리 dict_data를 위한 키 설정
keys = ['지역', '총인구수', '세대수', '세대당_인구', '남자_인구수', '여자_인구수', '남여_비율']

# 리스트 list_data와 딕셔너리의 키 keys를 딕셔너리 dict_data에 저장
pop.get_dict(list_data, keys, dict_data)              

frame = pd.DataFrame(dict_data)
frame2 = frame.iloc[:, [1, 2, 4, 5]]
print(frame2)

# sum() 메소드로 열 방향으로 합계를 구함
sum = frame2.sum(axis=0)
print(sum)

print('-' * 50)
print('국내 전체 인구 통계')
print('-' * 50)
print('- 총 인구수 : %d명' % sum.iloc[0])
print('- 총 세대수 : %d명' % sum.iloc[1])
print('- 총 남자 인구수 : %d명' % sum.iloc[2])
print('- 총 여자 인구수 : %d명' % sum.iloc[3])
print('-' * 50)