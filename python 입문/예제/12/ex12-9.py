import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='Malgun Gothic')

pets = ['개', '고양이', '기타', '기르지않음']
portion = [18, 3.4, 3.1, 75.5 ]

plt.pie(portion, explode=(0, 0.1, 0, 0), labels=pets, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('총 가구 대비 반려동물 기르는 비율(2018)')

plt.show()