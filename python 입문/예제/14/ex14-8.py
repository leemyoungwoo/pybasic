import pandas as pd

member = {'이름':['김영준','한지원'],
        '나이':[20, 23],
        '전화번호':['010-3535-4576', '010-1295-7899']}

frame = pd.DataFrame(member, columns=['이름', '전화번호', '나이', '주소'],
                    index=['01', '02'])
print(frame)