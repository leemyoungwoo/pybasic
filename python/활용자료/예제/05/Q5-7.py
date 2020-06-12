questions = ['tr_in', 'b_s', '_axi', 'air_lane']
answers   = ['a', 'u', 't','p']

for i in range(len(questions)) :
    q = '%s 에서 밑줄(_) 안에 들어갈 알파벳은?' % questions[i]
    ans = input(q)

    if ans == answers[i] :
        print('정답입니다!')
    else :
        print('틀렸습니다!')