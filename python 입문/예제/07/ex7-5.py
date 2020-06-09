# 서브 루틴 : func() 함수
def func(x) :
    x = 100
    print('func() : x = ', x, ', id =', id(x))

# 메인 루틴
x = 10
print('메인 : x = ', x, ', id =', id(x))
func(x)
print('메인 : x = ', x, ', id =', id(x))
