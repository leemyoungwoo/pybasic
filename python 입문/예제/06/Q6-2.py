admin_info = ('admin', '12345', 'rubato@naver.com')

id = input('관리자 아이디를 입력하세요 : ')
password = input('관리자 비밀번호를 입력하세요 : ')

if  id == admin_info[0] and password == admin_info[1] :
    print('관리자입니다.')
else :
    print('아이디 또는 비밀번호가 잘못 입력되었습니다.')