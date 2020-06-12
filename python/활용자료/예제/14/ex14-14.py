import population as pop

list_data = []

# CSV 파일을 읽어 들여 리스트 list_data에 저장
pop.get_list(list_data)         

dict_data = {}

# 딕셔너리 dict_data를 위한 키 설정
keys = ['지역', '총인구수', '세대수', '세대당_인구', '남자_인구수', '여자_인구수', '남여_비율']

# 리스트 list_data와 딕셔너리의 키 keys를 딕셔너리 dict_data에 저장
pop.get_dict(list_data, keys, dict_data)              

print(dict_data)