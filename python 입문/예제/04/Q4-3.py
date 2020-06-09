phone = input('하이픈(-)을 뺀 11자리의 휴대폰 번호를 입력하세요: ') 

number = '';
for i in range(0, len(phone)) :
    if i == 2 :
        number = number + (phone[2]+'-')
    elif i == 6 :
        number = number + (phone[6]+'-')
    else :
        number = number + phone[i]

print(number)