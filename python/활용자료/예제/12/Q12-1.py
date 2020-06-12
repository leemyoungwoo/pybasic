import matplotlib.pyplot as plt

date = list(range(1,11))
min_temp = [7.3, 3.5, 7.2, 4.5, 3.5, 8.3, 7.7, 6.4, 9.3, 6.3]
max_temp = [15, 16.3, 15.2, 17.5, 18.3, 20.0, 18.8, 17.5, 14.2, 15.3]

plt.plot(date, min_temp, label='Min Temparature', color='red', linestyle='-', marker='o')
plt.plot(date, max_temp, label='Max Temparature', color='blue', linestyle='-.', marker='x')
plt.legend(loc='best')
plt.xlabel('date')
plt.ylabel('temprature')

plt.title('Min and max temparature of ten days')
         
plt.show()