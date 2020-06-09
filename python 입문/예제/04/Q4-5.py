print('-' * 40) 
print('킬로그램(kg) 파운드(lb)   온스(oz)')
print('-' * 40) 

for kg in range(10, 101, 5) : 
    lb = kg * 2.204623
    oz = kg * 35.273962
    print('%8d  %10.1f %10.1f' % (kg, lb, oz))   
     
print('-' * 40)