i = 200
count = 0
while i < 601 :
    if i % 3 != 0 :
        print('%d ' % i, end='')
        count += 1
        if count % 8 == 0 :
            print()
    i += 1