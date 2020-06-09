print('서비스 만족도 :') 
print('  1: 매우만족') 
print('  2: 만족') 
print('  3: 불만족') 
a = input('서비스 만족도를 입력해주세요(예: 1 또는 2 또는 3) : ') 

price = int(input('음식값을 입력해 주세요(예:8000) : ')) 

if a == '1' : 
    tip = int(price * 0.2) 
    service = '매우 만족' 
elif a == '2' : 
    tip = int(price * 0.1) 
    service = '만족' 
else : 
    tip = int(price * 0.05) 
    service = '불만족' 

print()
print('서비스 만족도 : %s, 팁 : %d원' % (service, tip))