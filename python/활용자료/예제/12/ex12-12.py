import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='Malgun Gothic')

x = list(range(1,11))
y = list(range(10, 101, 10))

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(9, 5), sharex=True, sharey=True)
ax = axs[0][0]
ax.plot(x,y)
ax.set_title('선 그래프 1')

ax = axs[0][1]
ax.plot(x,y, color='red', linestyle='--', marker='o')
ax.set_title('선 그래프 2')

ax = axs[1][0]
ax.bar(x,y)
ax.set_title('막대 그래프')

ax = axs[1][1]
ax.scatter(x,y)
ax.set_title('산포 그래프')

plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.2, hspace=0.3)
plt.savefig('fig1.png')

plt.show()