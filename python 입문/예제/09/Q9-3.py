class Calculator :
    def __init__(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2
    
    def add(self) :
        return self.num1 + self.num2
    def sub(self) :
        return self.num1 - self.num2
    def mul(self) :
        return self.num1 * self.num2
    def div(self) :
        return self.num1 / self.num2

a = int(input('첫번째 수를 입력하세요 : '))
b = int(input('두번째 수를 입력하세요 : '))

cal1 = Calculator(a, b)
print('%d - %d = %d' % (a, b, cal1.sub()))
print('%d / %d = %.1f' % (a, b, cal1.div()))