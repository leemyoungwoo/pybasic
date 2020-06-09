import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='Malgun Gothic')

xdata = ['안지영', '홍지수', '황예린']
ydata1 = [90, 85, 88]
ydata2 = [83, 88, 91]
plt.plot(xdata, ydata1, label='국어')
plt.plot(xdata, ydata2, label='영어')
plt.legend(loc='upper center')

plt.title('세명 학생의 국어, 영어 성적')

plt.show()