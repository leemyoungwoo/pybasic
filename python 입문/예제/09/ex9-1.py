class Calculator :
    def set(self, x, y) :
        self.first = x
        self.second = y
    
    def add(self) :
        result = self.first + self.second
        return result
    
cal1 = Calculator()
   
cal1.set(10, 20)
print('%d + %d = %d' % (cal1.first, cal1.second, cal1.add()))
cal1.set(100, 200)
print('%d + %d = %d' % (cal1.first, cal1.second, cal1.add()))