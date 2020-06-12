class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print('이름:%s, 나이:%d' % (self.name, self.age))
        
    def getInfo(self) :
        return self.name + ', ' + str(self.age)
        
class Student(Person):
    def __init__(self, name, age, department, id):
        super().__init__(name, age)
        self.department = department
        self.id = id
        
    def printStudentInfo(self):
        name_age = super().getInfo()
        print(name_age)
        print('%s님의 학과:%s, 학번:%s' % (self.name, self.department, self.id))

x = Student('홍지수', 20, '소프트웨어공학과', '20215550001')
x.printInfo()
x.printStudentInfo()