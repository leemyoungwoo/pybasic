print('-' * 30) 
print('     섭씨     화씨')
print('-' * 30) 

c = -20
while c < 41 :
    f = c * 9.0/ 5.0 + 32.0 
    print('%8d  %8.1f' % (c, f))

    c +=1
     
print('-' * 30)