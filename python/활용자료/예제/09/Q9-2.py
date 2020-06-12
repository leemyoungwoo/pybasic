class SumAvg :
    title = '- 3과목 합계와 평균'
    def __init__(self, name, kor, eng, math) : 
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    
    def getSum(self) :
        sum = self.kor + self.eng + self.math
        return sum

s1 = SumAvg('김성윤', 85, 90, 83)

print(SumAvg.title)
print('이름 : %s' % s1.name)
print('국어 : %d, 영어 : %d, 수학 : %d' % (s1.kor, s1.eng, s1.math))
print('합계 : %d, 평균 : %.1f' % (s1.getSum(), s1.getSum()/3))