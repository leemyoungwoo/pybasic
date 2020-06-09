now_year  = int(input('현재년을 입력해 주세요 : ')) 
now_month = int(input('현재월을 입력해 주세요 : ')) 
now_day   = int(input('현재일을 입력해 주세요 : ')) 

birth_year  = int(input('출생년을 입력해 주세요 : ')) 
birth_month = int(input('출생월을 입력해 주세요 : ')) 
birth_day   = int(input('출생일을 입력해 주세요 : ')) 

if birth_month < now_month : 
    age = now_year - birth_year 
elif birth_month == now_month : 
    if birth_day < now_day : 
        age = now_year - birth_year 
    else : 
        age = now_year - birth_year - 1 
else : 
    age = now_year - birth_year - 1 

print('-' * 50) 
print('오늘 날짜 : %d년 %d월 %d일' % (now_year, now_month, now_day))
print('생년 월일 : %d년 %d월 %d일' % (birth_year, birth_month, birth_day))
print('-' * 50) 
print('만 나이 : %d세' % age) 
print('-' * 50)