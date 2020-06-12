class Person :
    def __init__(self, info) :
        self.info = info
    
    def getName(self) :
        return self.info[0]

    def getEmail(self) :
        return self.info[1]
    
    def getPhoneNum(self) :
        return self.info[2]

info = ['김지혜', 'rubato@hanmail.net', '010-1234-4567']
person = Person(info)

print('성명 : %s' % person.getName())
print('이메일 : %s' % person.getEmail())
print('전화번호 : %s' % person.getPhoneNum())