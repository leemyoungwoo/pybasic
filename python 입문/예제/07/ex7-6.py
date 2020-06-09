# 서브 루틴 : func() 함수
def func(x) :
    x[0] = 100
    print('func() : x = ', x, ', id =', id(x))

# 메인 루틴
x = [1, 2, 3]
print('메인 : x = ', x, ', id =', id(x))
func(x)
print('메인 : x = ', x, ', id =', id(x))