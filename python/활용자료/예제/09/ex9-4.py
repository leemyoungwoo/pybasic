class MyClass :
    def __init__(self, number) :
        self.number = number     # 인스턴스 속성
        
    def inc_10(self): 
        self.number += 10
  
    def inc_20(self): 
        self.number += 20
        
obj1 = MyClass(100) 
obj1.inc_10()         
obj1.inc_20()
print(obj1.number)
  
obj2 = MyClass(200) 
obj2.inc_10()     
obj2.inc_20() 
print(obj2.number)