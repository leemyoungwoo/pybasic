def circle_area(r) :
    area = r * r * 3.14
    
    return area

radius = int(input('원의 반지름을 입력하세요 : '))
result = circle_area(radius)
print('반지름 : %d, 원의 면적 : %.2f' % (radius, result))

radius = int(input('원의 반지름을 입력하세요 : '))
result = circle_area(radius)
print('반지름 : %d, 원의 면적 : %.2f' % (radius, result))     
