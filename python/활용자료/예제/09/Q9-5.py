class EngSentence :
    def __init__(self, sentence) :
        self.sentence = sentence
        self.length = len(self.sentence)
    
    def reverse(self) :
        tmp = ''
        for i in range(self.length) :
            tmp += (self.sentence[self.length-1 -i])
        return tmp
    
    def insertHypen(self) :
        tmp = ''
        for i in range(self.length) :
            if self.sentence[i] == ' ' :
                tmp += '-'
            else :
                tmp += self.sentence[i]
        return tmp
        
a = 'We are the champions!'
eng1 = EngSentence(a)
print('역순 : %s' % eng1.reverse())
print('하이픈(-) 삽입 : %s' % eng1.insertHypen())