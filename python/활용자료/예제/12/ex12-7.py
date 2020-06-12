import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='Malgun Gothic')

x = ['영희', '철수', '재호']
y = [3, 1, 5]
plt.title('연간 영화관람 회수')
plt.bar(x, y)
plt.ylabel('회수')
plt.show()