import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='Malgun Gothic')

x = ['월', '화', '수', '목', '금', '토', '일']
y = [6.5, 5.7, 5.5, 6.7, 6.3, 7.5, 8.3]
plt.title('연간 요일별 평균 수면시간')
plt.scatter(x, y)
plt.ylabel('수면시간')
plt.show()