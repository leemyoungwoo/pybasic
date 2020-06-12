s = input('영어 문장을 입력하세요 :')

i = 0
count = 0

print('모음 : ', end = '')

while i <= len(s) - 1 :
    if (s[i] == 'a' or s[i] == 'A'  or s[i] == 'e' or s[i] == 'E' \
        or  s[i] == 'i' or s[i] == 'I' or s[i] == 'o' or s[i] == 'O' \
        or s[i] == 'u' or s[i] == 'U') :
        count += 1
        print(s[i], end=' ')
        
    i += 1
    
print('\n모음의 개수 : %d' % count)