import matplotlib.pyplot as plt
from matplotlib import rc
import random

rc('font', family='Malgun Gothic')

def make_random_list(num):
    result = []
    for i in range(num):
        result.append(random.randrange(1,7))
    return result

count = 10          # 주사위 던진 회수
y = make_random_list(count)
x = list(range(1,11))

plt.title('주사위 10회 던지기')
plt.bar(x, y)
plt.xticks(x)
plt.yticks([1, 2, 3, 4, 5, 6])
plt.xlabel('던진 회수')
plt.ylabel('주사위 눈')

plt.show()