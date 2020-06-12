import math

class Circle :
    def __init__(self, radius) :
        self.radius = radius
    
    def getArea(self) :
        area = math.pi * self.radius * self.radius
        return area

    def getCircum(self) :
        circum = 2 * 3.141592 * self.radius
        return circum
        
cir = Circle(10)

print('반지름: %d' % cir.radius)
print('원의 면적 : %.2f' % cir.getArea())
print('원주의 길이 : %.2f' % cir.getCircum())