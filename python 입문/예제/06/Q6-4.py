ad = {'id':'admin', 'password':'11111'}

in_id = input('아이디를 입력하세요: ')
in_password = input('비밀번호를 입력하세요: ')

if (in_id == ad['id'] and in_password == ad['password']) :
    print('모든 정보에 접근 가능합니다!')
else :
    print('정보에 접근 권한이 없습니다!')