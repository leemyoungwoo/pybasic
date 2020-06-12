import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='Malgun Gothic')

xdata = ['안지영', '홍지수', '황예린']
ydata1 = [90, 85, 88]
ydata2 = [83, 88, 91]
ydata3 = [85, 97, 78]
ydata4 = [92, 88, 82]

plt.plot(xdata, ydata1, label='국어', color='red', linestyle='-', marker='o')
plt.plot(xdata, ydata2, label='영어', color='#00ffff', linestyle='--', marker='x')
plt.plot(xdata, ydata3, label='수학', color='magenta', linestyle='-.', marker='s')
plt.plot(xdata, ydata4, label='사회', color='#444444', linestyle=':', marker='d')

plt.title('세명 학생의 네 과목 성적')
plt.legend(loc='best')

plt.show()