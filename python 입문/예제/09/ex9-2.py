class Member :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def showMember(self) :
        print('이름 : %s' % self.name)
        print('나이 : %d' % self.age)
        
mem1 = Member('홍지수', 24)
mem1.showMember()
mem2 = Member('안지영', 20)
mem2.showMember()