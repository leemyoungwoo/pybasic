import matplotlib.pyplot as plt

xdata = list(range(30))
ydata = []

for x in xdata:
    y = 2 * x
    ydata.append(y)

plt.plot(xdata, ydata, label='y=2x')
plt.xlim(0, 35)
plt.ylim(0, 70)
plt.xticks(list(range(0, 35, 2)))
plt.yticks(list(range(0, 70, 5)))

plt.grid(True)
plt.show()