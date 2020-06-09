import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='Malgun Gothic')

font1 = {'size':18, 'color':'green'}

xdata = ['안지영', '홍지수', '황예린']
ydata = [90, 85, 88]
plt.plot(xdata, ydata)

plt.title('세명 학생의 국어 성적', fontdict=font1)
plt.xlabel('이름')
plt.ylabel('성적')

plt.show()