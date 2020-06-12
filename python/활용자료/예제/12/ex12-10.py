import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='Malgun Gothic')

x = ['월', '화', '수', '목', '금', '토', '일']
y1 = [6.5, 5.7, 5.5, 6.7, 6.3, 7.5, 8.3]
y2 = [6.3, 7.7, 7.5, 7.7, 6.2, 7.3, 8.5]

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 3), sharex=True, sharey=True)
ax = axs[0]
ax.scatter(x,y1)
ax.set_title('2018')

ax = axs[1]
ax.scatter(x,y2)
ax.set_title('2019')

fig.suptitle('연간 요일별 평균 수면시간')

plt.show()