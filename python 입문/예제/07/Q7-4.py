def matchWord(word, answer) : 
   if word == answer : 
      msg = '맞습니다!' 
   else : 
      msg = '틀렸습니다!' 
   return msg 

eng_dict = {'orange':'오렌지', 'cookie':'과자', 'mother':'어머니', 'brother':'형제', 'python':'파이썬'} 

for key in eng_dict : 
    string = input(eng_dict[key] + '에 맞는 영어 단어는? ') 
    result = matchWord(string, key) 
    print(result)